# =============================================================================
# Unified GCP Terraform Infrastructure - Serverless Chunked QuantConnect Poller
# =============================================================================
# Contains ALL GCP Infrastructure in one single main file:
# 1. API Services Enablement
# 2. Dedicated IAM Service Account & Role Assignments
# 3. GCP Secret Manager for QuantConnect API Credentials
# 4. Source Storage Bucket & Cloud Function (2nd Gen) Source Zip
# 5. Cloud Function (2nd Gen) with STRICT COST CONTROL:
#    - min_instance_count = 0 (Billed $0 when idle)
#    - max_instance_count = 1 (Hard ceiling preventing scaling runaways)
#    - memory = 256Mi (Minimal footprint)
# 6. GCP Cloud Scheduler Cron Job (Runs every 5 minutes)
# =============================================================================

terraform {
  required_version = ">= 1.3.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.0"
    }
  }
}

provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

# -----------------------------------------------------------------------------
# 1. GCP API Services Enablement
# -----------------------------------------------------------------------------
resource "google_project_service" "apis" {
  for_each = toset([
    "cloudfunctions.googleapis.com",
    "run.googleapis.com",
    "cloudscheduler.googleapis.com",
    "bigquery.googleapis.com",
    "secretmanager.googleapis.com",
    "storage.googleapis.com",
    "iam.googleapis.com",
  ])

  service            = each.key
  disable_on_destroy = false
}

# -----------------------------------------------------------------------------
# 2. Service Account & IAM Roles
# -----------------------------------------------------------------------------
resource "google_service_account" "poller_sa" {
  account_id   = "qc-batch-poller-sa"
  display_name = "QuantConnect Batch Poller Service Account"
  depends_on   = [google_project_service.apis]
}

resource "google_project_iam_member" "bq_editor" {
  project = var.gcp_project_id
  role    = "roles/bigquery.dataEditor"
  member  = "serviceAccount:${google_service_account.poller_sa.email}"
}

resource "google_project_iam_member" "bq_job_user" {
  project = var.gcp_project_id
  role    = "roles/bigquery.jobUser"
  member  = "serviceAccount:${google_service_account.poller_sa.email}"
}

# -----------------------------------------------------------------------------
# 3. Secret Manager for QuantConnect API Credentials
# -----------------------------------------------------------------------------
resource "google_secret_manager_secret" "qc_api_key" {
  secret_id = "qc-login-api-key"
  replication {
    auto {}
  }
  depends_on = [google_project_service.apis]
}

resource "google_secret_manager_secret_version" "qc_api_key_version" {
  secret      = google_secret_manager_secret.qc_api_key.id
  secret_data = var.qc_login_api_key
}

resource "google_secret_manager_secret_iam_member" "sa_secret_access" {
  secret_id = google_secret_manager_secret.qc_api_key.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.poller_sa.email}"
}

# -----------------------------------------------------------------------------
# 4. Storage Bucket & Code Source Archive
# -----------------------------------------------------------------------------
resource "google_storage_bucket" "source_bucket" {
  name                        = "${var.gcp_project_id}-qc-poller-source"
  location                    = var.gcp_region
  force_destroy               = true
  uniform_bucket_level_access = true
  depends_on                  = [google_project_service.apis]
}

data "archive_file" "function_source_zip" {
  type        = "zip"
  source_dir  = "${path.module}/src"
  output_path = "${path.module}/function_source.zip"
}

resource "google_storage_bucket_object" "source_zip_object" {
  name   = "source-${data.archive_file.function_source_zip.output_md5}.zip"
  bucket = google_storage_bucket.source_bucket.name
  source = data.archive_file.function_source_zip.output_path
}

# -----------------------------------------------------------------------------
# 5. Cloud Function (2nd Gen) with STRICT COST CONTROL & RUNAWAY PREVENTION
# -----------------------------------------------------------------------------
resource "google_cloudfunctions2_function" "qc_batch_poller_func" {
  name        = "qc-batch-poller-function"
  location    = var.gcp_region
  description = "Serverless QuantConnect Batch Poller & BigQuery Ingestor"

  build_config {
    runtime     = "python310"
    entry_point = "handle_batch_poll"
    source {
      storage_source {
        bucket = google_storage_bucket.source_bucket.name
        object = google_storage_bucket_object.source_zip_object.name
      }
    }
  }

  service_config {
    # COST CONTROL & RUNAWAY PREVENTION GUARANTEES:
    min_instance_count               = 0    # 0 instances when idle -> BILLED $0 WHEN IDLE
    max_instance_count               = 1    # Hard limit of 1 max instance -> PREVENTS SCALING COST RUNAWAYS
    available_memory                 = "256Mi" # Smallest memory footprint
    timeout_seconds                  = 60   # Max execution duration limit
    max_instance_request_concurrency = 1
    service_account_email            = google_service_account.poller_sa.email

    environment_variables = {
      BIGQUERY_PROJECT        = var.gcp_project_id
      BIGQUERY_DATASET        = var.bigquery_dataset_id
      QUANTCONNECT_USER_ID    = var.qc_user_id
      QUANTCONNECT_PROJECT_ID = var.qc_project_id
    }

    secret_environment_variables {
      key        = "QUANTCONNECT_LOGIN_API_KEY"
      project_id = var.gcp_project_id
      secret     = google_secret_manager_secret.qc_api_key.secret_id
      version    = "latest"
    }
  }

  depends_on = [
    google_project_service.apis,
    google_secret_manager_secret_version.qc_api_key_version,
    google_secret_manager_secret_iam_member.sa_secret_access
  ]
}

# Cloud Run Invoker role for Service Account to invoke function
resource "google_cloud_run_service_iam_member" "invoker" {
  location = google_cloudfunctions2_function.qc_batch_poller_func.location
  service  = google_cloudfunctions2_function.qc_batch_poller_func.name
  role     = "roles/run.invoker"
  member   = "serviceAccount:${google_service_account.poller_sa.email}"
}

# -----------------------------------------------------------------------------
# 6. GCP Cloud Scheduler Cron Job (Runs every 5 minutes)
# -----------------------------------------------------------------------------
resource "google_cloud_scheduler_job" "poller_cron" {
  name        = "qc-batch-poller-cron"
  description = "Triggers qc-batch-poller-function every 5 minutes"
  schedule    = var.cron_schedule
  time_zone   = "UTC"
  region      = var.gcp_region

  http_target {
    http_method = "POST"
    uri         = google_cloudfunctions2_function.qc_batch_poller_func.service_config[0].uri
    headers = {
      "Content-Type" = "application/json"
    }
    body = base64encode(jsonencode({ trigger = "cloud_scheduler" }))

    oidc_token {
      service_account_email = google_service_account.poller_sa.email
    }
  }

  depends_on = [
    google_cloudfunctions2_function.qc_batch_poller_func,
    google_cloud_run_service_iam_member.invoker
  ]
}

# -----------------------------------------------------------------------------
# Outputs
# -----------------------------------------------------------------------------
output "function_uri" {
  value       = google_cloudfunctions2_function.qc_batch_poller_func.service_config[0].uri
  description = "HTTP URI of the 2nd Gen Cloud Function"
}

output "scheduler_job_name" {
  value       = google_cloud_scheduler_job.poller_cron.name
  description = "Name of the Cloud Scheduler cron job"
}

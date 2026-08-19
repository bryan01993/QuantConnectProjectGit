variable "gcp_project_id" {
  type        = string
  description = "GCP Project ID"
  default     = "bav-personal-cloud"
}

variable "gcp_region" {
  type        = string
  description = "GCP Region for Cloud Function & Scheduler"
  default     = "europe-west1"
}

variable "bigquery_dataset_id" {
  type        = string
  description = "BigQuery Dataset ID"
  default     = "develop"
}

variable "qc_login_api_key" {
  type        = string
  description = "QuantConnect LOGIN API KEY"
  sensitive   = true
  default     = "e9976a652350e58267cae49c0125e0e76e6a3fd712ef327ef4f3ee44742a45d3"
}

variable "qc_user_id" {
  type        = string
  description = "QuantConnect USER ID"
  default     = "116616"
}

variable "qc_project_id" {
  type        = string
  description = "QuantConnect PROJECT ID"
  default     = "22447448"
}

variable "cron_schedule" {
  type        = string
  description = "Cron schedule for Cloud Scheduler polling (default: every 5 minutes)"
  default     = "*/5 * * * *"
}

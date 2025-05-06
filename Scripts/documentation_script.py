# import os
# import shutil
#
# def rename_and_copy_py_files(src_dir, output_dir="output_documentation"):
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#
#     found_files = []
#
#     print(f"🔍 Scanning in: {src_dir}")
#     for root, dirs, files in os.walk(src_dir):
#         print(f"📁 Entering: {root}")
#         for file in files:
#             if file.endswith(('.pyi')):
#                 full_path = os.path.join(root, file)
#                 found_files.append(full_path)
#
#                 relative_path = os.path.relpath(root, src_dir)
#                 path_parts = [] if relative_path == '.' else relative_path.split(os.sep)
#                 new_name = "_".join(path_parts + ["file", file])
#                 dst_file_path = os.path.join(output_dir, new_name)
#                 shutil.copy2(full_path, dst_file_path)
#
#     print("\n✅ Found Python Files:")
#     for f in found_files:
#         print(f)
#
# # Example usage
# rename_and_copy_py_files("./Docu/QuantConnect")


import os

def concatenate_documentation_files(source_dir="output_documentation", output_file="combined_documentation.pyi"):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_name in sorted(os.listdir(source_dir)):
            if file_name.endswith(('.py', '.pyi')):
                file_path = os.path.join(source_dir, file_name)
                outfile.write(f"# ===== From: {file_name} =====\n")
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write("\n\n")  # Add spacing between files

    print(f"✅ Combined documentation saved to: {output_file}")

# Example usage
concatenate_documentation_files()
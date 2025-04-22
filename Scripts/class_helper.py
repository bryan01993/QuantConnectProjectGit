import os

def find_pyi_files(root_dir):
    pyi_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith('.pyi'):
                pyi_files.append(os.path.join(dirpath, file))
    return pyi_files

# Example usage
if __name__ == "__main__":
    root_directory = "C:/Users/bryan/PycharmProjects/QuantConnectProject/.venv/Lib/site-packages/QuantConnect"  # or replace with full path like "C:/Users/bryan/PyCharmProjects/QuantConnectProject"
    results = find_pyi_files(root_directory)
    for path in results:
        print(path)

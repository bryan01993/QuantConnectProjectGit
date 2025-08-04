import os


def find_pyi_files(root_dir):
    """Return a list of ``.pyi`` files within ``root_dir``.

    Pseudocode:
        initialize empty list for results
        walk through directories under ``root_dir``
        for each file encountered:
            if file extension is ``.pyi``:
                append absolute path to results list
        return collected paths
    """
    pyi_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(".pyi"):
                pyi_files.append(os.path.join(dirpath, file))
    return pyi_files


if __name__ == "__main__":
    ROOT_DIRECTORY = (
        "C:/Users/bryan/PycharmProjects/QuantConnectProject/.venv/"
        "Lib/site-packages/QuantConnect"
    )
    for path in find_pyi_files(ROOT_DIRECTORY):
        print(path)

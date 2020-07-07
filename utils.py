import os


def delete_files(filepath: str, file_ext):
    xml_files = (f for f in os.listdir(filepath) if f.endswith(f".{file_ext}"))
    for file in xml_files:
        os.remove(os.path.join(filepath, file))

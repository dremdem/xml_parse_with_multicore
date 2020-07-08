import os
import string
import random
import argparse


def delete_files(filepath: str, file_ext):
    xml_files = (f for f in os.listdir(filepath) if f.endswith(f".{file_ext}"))
    for file in xml_files:
        os.remove(os.path.join(filepath, file))


def get_random_string() -> str:
    string_length = random.randint(5, 30)
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_length))


def get_random_unique_string(string_list: list) -> str:
    unique_string = None
    while unique_string in string_list if unique_string else True:
        unique_string = get_random_string()

    return unique_string


def check_path(filepath):
    if os.path.isdir(filepath):
        return filepath
    else:
        raise argparse.ArgumentTypeError('Filename "%s" doesn\'t exist' % filepath)

"""
Various utils for daily usage
"""

import os
import logging
import string
import random
from logging.handlers import RotatingFileHandler
import argparse


def log_setup():
    """
    Setup logging environment: console and rotating files
    :return:
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    file_logger = RotatingFileHandler("mp.log", maxBytes=5000, backupCount=10)
    file_logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        u'[%(asctime)s]  %(message)s')
    file_logger.setFormatter(formatter)
    root_logger.addHandler(file_logger)

    console_logger = logging.StreamHandler()
    console_logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    console_logger.setFormatter(formatter)
    root_logger.addHandler(console_logger)


def delete_files(filepath: str, file_ext: str):
    """Delete files with the certain extension"""
    xml_files = (f for f in os.listdir(filepath) if f.endswith(f".{file_ext}"))
    for file in xml_files:
        os.remove(os.path.join(filepath, file))


def get_random_string() -> str:
    """ Get a random string with uppercase chars and digits"""
    string_length = random.randint(5, 30)
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_length))


def get_random_unique_string(string_list: list) -> str:
    """ Get a unique random string, check in the list """
    unique_string = None
    while unique_string in string_list if unique_string else True:
        unique_string = get_random_string()

    return unique_string


def check_path(filepath):
    """Check for path existence"""
    if os.path.isdir(filepath):
        return filepath
    else:
        raise argparse.ArgumentTypeError('Filename "%s" doesn\'t exist' % filepath)

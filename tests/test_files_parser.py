import pathlib

from files_parser import parse_all_files

filepath = pathlib.Path().absolute()


def test_parse_all_files():
    parse_all_files(filepath)

    assert False

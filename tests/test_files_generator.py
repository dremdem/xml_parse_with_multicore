import pathlib

from files_generator import generate_xml_file, get_random_string, get_random_unique_string, generate_zip_file

filepath = pathlib.Path().absolute()


def test_generate_xml_file():
    string_list = []
    generate_xml_file(string_list)
    assert False


def test_get_random_string():
    get_random_string()
    assert False


def test_get_random_unique_string():
    string_list = ['qweqwe', 'qweqweasdad!@#']
    random_unique_string = get_random_unique_string(string_list)
    assert random_unique_string not in string_list


def test_generate_zip_file():
    id_list = []
    generate_zip_file('zip1.zip', filepath, 100, id_list)


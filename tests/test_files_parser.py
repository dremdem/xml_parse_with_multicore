import pathlib

from files_parser import parse_all_files, read_xml_file, read_zip_file, read_zip_files, parse_chunk

filepath = pathlib.Path().absolute()


def test_parse_all_files():
    parse_all_files(filepath)
    assert False


def test_read_xml_file():
    xml = read_xml_file('x_1.xml')
    assert False


def test_read_zip_file():
    zip_list = []
    zip_list += read_zip_file('zip1.zip', zip_list)
    assert False


def test_read_zip_files():
    main_list = read_zip_files(filepath)
    print(main_list)
    assert False


def test_parse_chunk():
    main_list = read_zip_files(filepath)
    (c1, c2) = parse_chunk(main_list)

    print(c1, c2)
    assert False

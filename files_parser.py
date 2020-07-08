"""
Parse ZIP-files by using multi-core processing
"""

import os
import sys
import csv
import zipfile
import xml.etree.cElementTree as ET


def read_xml_file(xml_file) -> dict:
    xml_dict = {}

    xml = ET.parse(xml_file)
    root = xml.getroot()

    xml_dict['id'] = root.find('var[@name="id"]').get('value')
    xml_dict['level'] = root.find('var[@name="level"]').get('value')

    xml_dict['objects'] = [o.get('name') for o in root.findall('object')]

    return xml_dict


def read_zip_file(filename: str) -> list:
    zip_list = []

    with zipfile.ZipFile(filename) as z:
        for xml_file in [f.filename for f in z.infolist()]:
            with z.open(xml_file) as x:
                zip_list += [read_xml_file(x)]

    return zip_list


def read_zip_files(filepath: str, pool, cores_quantity, use_mp: bool = False) -> list:
    main_list = []

    zip_files = [f for f in next(os.walk(filepath))[2] if f.endswith('.zip')]

    if use_mp:
        chunk_size = len(zip_files) // cores_quantity
        zip_files_chunks = list(list_by_chunks(zip_files, chunk_size))
        for chunk in zip_files_chunks:
            res = [pool.apply_async(read_zip_file, (file,)) for file in chunk]
            for i in res:
                main_list += i.get()
    else:
        for file in [f for f in next(os.walk(filepath))[2] if f.endswith('.zip')]:
            main_list += read_zip_file(file)

    print(f'sys.getsizeof(main_list): {sys.getsizeof(main_list)}, len: {len(main_list)}')

    return main_list


def write_csv_file(filename: str, csv_list: list):
    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerows(csv_list)


def parse_chunk(zip_list):
    csv_list1 = []
    csv_list2 = []

    for element in zip_list:

        id = element['id']
        level = element['level']
        csv_list1 += [[id, level]]

        for o in element['objects']:
            csv_list2 += [[id, o]]

    return csv_list1, csv_list2


def list_by_chunks(main_list, size_of_chuck):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(main_list), size_of_chuck):
        yield main_list[i:i + size_of_chuck]


def parse_all_files(filepath: str, pool, cores_quantity, use_mp: bool = False):
    """
    Parse all ZIP-file by filepath
    """

    # Structure of element in a main list:
    # [{id: '<id>', 'level': <level>, 'objects': [<object_name1>, <object_name2>], ... }]

    main_list = read_zip_files(filepath, pool, cores_quantity, use_mp=use_mp)

    if use_mp:
        len_of_chunk = len(main_list) // cores_quantity

        list_of_chunks = list(list_by_chunks(main_list, len_of_chunk))
        results = [pool.apply_async(parse_chunk, (l1,)) for l1 in list_of_chunks]
        csv_list1 = []
        csv_list2 = []

        for chunk in results:
            for i in chunk.get():
                csv_list1 += i[0]
                csv_list2 += i[1]
    else:
        csv_list1, csv_list2 = parse_chunk(main_list)

    write_csv_file(os.path.join(filepath, 'output1.csv'), csv_list1)
    write_csv_file(os.path.join(filepath, 'output2.csv'), csv_list2)

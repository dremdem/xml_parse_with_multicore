"""
Generate ZIP and XML files
"""
import random
import zipfile
import os
import xml.etree.cElementTree as ET

from utils import delete_files, get_random_string, get_random_unique_string


def generate_xml_file(filename: str, id_list: list):
    root = ET.Element('root')
    ET.SubElement(root, "var", attrib={"name": 'id', 'value': get_random_unique_string(id_list)})
    ET.SubElement(root, "var", attrib={"name": 'level', 'value': str(random.randint(1, 100))})

    objects_quantity = random.randint(1, 10)

    for _ in range(objects_quantity):
        ET.SubElement(root, "object", attrib={"name": get_random_string()})

    ET.ElementTree(root).write(filename)


def generate_zip_file(filename: str, filepath: str, number_of_xml: int, id_list: list):
    """

    :return: filepath to newly created file
    """

    for i in range(number_of_xml):
        generate_xml_file(f'x_{i+1}.xml', id_list)

    z = zipfile.ZipFile(os.path.join(filepath, filename), mode='w')
    for file in [f for f in next(os.walk(filepath))[2] if f.endswith('.xml')]:
        z.write(file)

    z.close()

    delete_files(filepath, 'xml')

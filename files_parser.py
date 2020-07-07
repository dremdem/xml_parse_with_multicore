"""
Parse ZIP-files by using multi-core processing
"""

import os
import csv


def write_csv_file(filename: str, csv_list: list):
    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerows(csv_list)


def parse_all_files(filepath: str):
    """
    Parse all ZIP-file by filepath
    """

    csv_list1 = []
    csv_list2 = []

    write_csv_file(os.path.join(filepath, 'output1.csv'), csv_list1)
    write_csv_file(os.path.join(filepath, 'output2.csv'), csv_list2)


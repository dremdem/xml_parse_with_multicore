"""
Main module for the test task
"""

import sys
import pathlib
import timeit


from files_generator import generate_zip_file
from files_parser import parse_all_files

if __name__ == '__main__':

    try:
        filepath = sys.argv[1]
    except IndexError:
        filepath = pathlib.Path().absolute()

    try:
        number_of_zip = int(sys.argv[2])
    except IndexError:
        number_of_zip = 50

    try:
        number_of_xml = int(sys.argv[2])
    except IndexError:
        number_of_xml = 100

    print(filepath)

    # generate ZIP-files

    id_list = []
    for i in range(number_of_zip):
        generate_zip_file(f'z_{i+1}.zip', filepath, number_of_xml, id_list)

    # parse ZIP-files
    start = timeit.default_timer()
    parse_all_files(filepath)
    stop = timeit.default_timer()
    execution_time = stop - start

    print(f"Parse done. Execution time is {round(execution_time, 3)} seconds.")


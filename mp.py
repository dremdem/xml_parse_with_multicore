"""
Main module for the test task
"""

import sys
import pathlib
import timeit
import multiprocessing


from files_generator import generate_zip_file
from files_parser import parse_all_files
from utils import delete_files


if __name__ == '__main__':
    cores_quantity = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores_quantity)

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

    delete_files(filepath, 'zip')

    # generate ZIP-files

    id_list = []
    for i in range(number_of_zip):
        generate_zip_file(f'z_{i+1}.zip', filepath, number_of_xml, id_list)

    # parse ZIP-files
    start = timeit.default_timer()
    parse_all_files(filepath, pool, cores_quantity)
    stop = timeit.default_timer()
    execution_time = stop - start

    print(f"Parse done. Execution time is {round(execution_time, 3)} seconds.")


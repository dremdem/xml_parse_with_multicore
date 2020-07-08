"""
Main module for the test task
"""
import argparse
import pathlib
import timeit
import multiprocessing

from files_generator import generate_zip_file
from files_parser import parse_all_files
from utils import delete_files, check_path

if __name__ == '__main__':
    number_of_cores = multiprocessing.cpu_count()

    parser = argparse.ArgumentParser(
        description='XML generator and parser with a multiprocessing feature.')
    parser.add_argument('-fp', dest='filepath', type=check_path, default=pathlib.Path().absolute(),
                        help='File path for storing and reading XML-files. Current path by default.')
    parser.add_argument('-zn', dest='number_of_zip', type=int, default=50,
                        help='Number of ZIP-files for testing. 50 by default.')
    parser.add_argument('-xn', dest='number_of_xml', type=int, default=100,
                        help='Number of XML-files in the every ZIP-file. 100 by default.')
    parser.add_argument('-mp', dest='use_mp', action='store_true',
                        help='Enable multiprocessing. Disabled bay default.')
    parser.add_argument('-cn', dest='number_of_cores', type=int, default=number_of_cores,
                        help=f'Number of cores. {number_of_cores} by default')

    args = parser.parse_args()
    pool = multiprocessing.Pool(processes=args.number_of_cores)

    delete_files(args.filepath, 'zip')

    # generate ZIP-files
    start = timeit.default_timer()
    id_list = []
    for i in range(args.number_of_zip):
        generate_zip_file(f'z_{i + 1}.zip', args.filepath, args.number_of_xml, id_list)
    stop = timeit.default_timer()
    execution_time = stop - start
    print(f"The ZIP-generation is done. Execution time is {round(execution_time, 3)} seconds.")

    # parse ZIP-files
    start = timeit.default_timer()
    parse_all_files(args.filepath, pool, args.number_of_cores, use_mp=args.use_mp)
    stop = timeit.default_timer()
    execution_time = stop - start
    print(f"The ZIP-parsing is done. Execution time is {round(execution_time, 3)} seconds.")

    delete_files(args.filepath, 'zip')

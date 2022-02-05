import logging
import os
import glob
from util import generate_data_file_name, get_table_name_from_data_file, check_if_table_exists, DATA_FILE_SUFFIX
from errors import throw_table_does_not_exist, throw_table_already_exists


def create(table):
    if check_if_table_exists(table):
        throw_table_already_exists(table)
    else:
        f = open(generate_data_file_name(table), 'w+')
        logging.info(f"{table} is created.")
        f.close()
        return

def drop(table):
    if check_if_table_exists(table):
        os.remove(generate_data_file_name(table))
        logging.info(f"{table} is dropped.")
        return
    else:
        throw_table_does_not_exist(table)

def truncate(table):
    if check_if_table_exists(table):
        f = open(generate_data_file_name(table), 'w+')
        f.close()
        logging.info(f"{table} is truncated.")
        return
    else:
        throw_table_does_not_exist(table)

def list():
    list_of_datafiles = glob.glob('*'+DATA_FILE_SUFFIX)
    for item in list_of_datafiles:
        print(get_table_name_from_data_file(item))
    return
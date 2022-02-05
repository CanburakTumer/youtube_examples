import logging
import os
import json
from errors import throw_input_data_is_corrupted, throw_table_does_not_exist

DATA_FILE_SUFFIX = '.db'

def generate_data_file_name(table):
    return table+DATA_FILE_SUFFIX

def get_table_name_from_data_file(data_file):
    return data_file.replace(DATA_FILE_SUFFIX,'')

def split_data(data):
    splitted = data.split(",")
    if len(splitted) != 2:
        throw_input_data_is_corrupted()
    return splitted[0], splitted[1]

def check_if_table_exists(table):
    data_file_name = generate_data_file_name(table)
    if os.path.exists(data_file_name):
        return True
    return False

def read_table_into_json(table):
    if not check_if_table_exists(table):
        throw_table_does_not_exist(table)
    
    data_file = generate_data_file_name(table)
    with open(data_file, 'r') as f:
        file_data = f.read()
    return json.loads(file_data) if not file_data == "" else {}

def write_json_into_table(table, json_data):
    if not check_if_table_exists(table):
        throw_table_does_not_exist(table)
    
    data_file = generate_data_file_name(table)
    with open(data_file, 'w') as f:
        f.write(json.dumps(json_data))
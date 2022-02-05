import logging

TABLE_DOES_NOT_EXIST = 1
TABLE_ALREADY_EXISTS = 2
INPUT_DATA_IS_CORRUPTED = 3
KEY_ALREADY_EXISTS = 4
KEY_DOES_NOT_EXIST = 5
THIS_WILL_TRUNCATE_TABLE = 6

def throw_table_does_not_exist(table):
    logging.error(f"{table} does not exist.")
    exit(TABLE_DOES_NOT_EXIST)

def throw_table_already_exists(table):
    logging.error(f"{table} already exists.")
    exit(TABLE_ALREADY_EXISTS)

def throw_input_data_is_corrupted():
    logging.error("Input data is corrupted.")
    exit(INPUT_DATA_IS_CORRUPTED)

def throw_key_already_exists(key):
    logging.error(f"Key {key} already exists in table.")
    exit(KEY_ALREADY_EXISTS)

def throw_key_does_not_exist(key):
    logging.error(f"Key {key} does not exist in table.")
    exit(KEY_DOES_NOT_EXIST)

def throw_this_will_truncate_table(table):
    logging.error(f"This will truncate {table}")
    exit(THIS_WILL_TRUNCATE_TABLE)
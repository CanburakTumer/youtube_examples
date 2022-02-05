import logging
from util import split_data, read_table_into_json, write_json_into_table
from errors import throw_key_already_exists, throw_key_does_not_exist, throw_this_will_truncate_table

def insert(table,data):
    json_data = read_table_into_json(table)

    key, value = split_data(data)
    if key in json_data:
        throw_key_already_exists(key)

    json_data[key] = value
    write_json_into_table(table, json_data)
    logging.info(f"Data inserted. {key},{value}")

    return

def update(table, data, cond):
    json_data = read_table_into_json(table)

    if cond == None:
        for item in json_data:
            json_data[item] = data
        write_json_into_table(table, json_data)
        logging.info(f"All rows updated to {data}")
        return

    if cond in json_data:
        json_data[cond] = data
        write_json_into_table(table, json_data)
        logging.info(f"Data updated. {cond},{data}")
    else:
        throw_key_does_not_exist(cond)

    return
    

def select(table, cond):

    json_data = read_table_into_json(table)
    if cond == None:
        print(json_data)
    else:
        if cond in json_data:
            print(json_data[cond])
        else:
            print()

    return

def delete(table, cond):
    json_data = read_table_into_json(table)
    
    if cond == None:
        throw_this_will_truncate_table(table)

    if cond in json_data:
        json_data.pop(cond)
        logging.info(f"Key '{cond}' is deleted.")
    else:
        throw_key_does_not_exist(cond)
    write_json_into_table(table, json_data)
#!/usr/bin/env python
import click
from ddl import create, drop, truncate, list
from dml import insert, update, select, delete
import logging

logging.getLogger().setLevel(logging.INFO)

@click.command()
@click.argument('operation')
@click.option('--table')
@click.option('--cond', help='Condition for filtering data on key for select, delete and update operations')
@click.option('--data',help='Data to insert or update. seperated by comma e.g. key,value')
def dbms(operation, table, cond, data):
    logging.info(f"{operation} will be executed with following options. Table: {table}, Data: {data}, Cond: {cond}")
    if operation == 'create':
        create(table)
    elif operation == 'drop':
        drop(table)
    elif operation == 'truncate':
        truncate(table)
    elif operation == 'insert':
        insert(table, data)
    elif operation == 'update':
        update(table, data, cond)    
    elif operation == 'select':
        select(table, cond)
    elif operation == 'delete':
        delete(table, cond)
    elif operation == 'list':
        list()
    else:
        print("Command not registered.") 
    

if __name__ == '__main__':
    dbms()
## Simple DB  
This is a simple and sample DBMS I patched together in couple hours to demonstrate what is a DBMS. It will not evolve any further nor bugs will be fixed. This project may not follow best practices (e.g. it does not have tests, it is not OOP so on.)

It is just a key-value store, to demonstrate how DBMS helps us to store, access and edit data.

### Commands  
#### DDL
`./simple_db.py list` Lists all the tables.  
`./simple_db.py create --table <TABLE_NAME>`: Creates a table with name `<TABLE_NAME>`.  
`./simple_db.py drop --table <TABLE_NAME>`: Deletes the table with name `<TABLE_NAME>`.  
`./simple_db.py truncate --table <TABLE_NAME>`: Deletes all data from table `<TABLE_NAME>`.  

#### DML
`./simple_db.py insert --table <TABLE_NAME> --data <KEY,VALUE>`: Inserts data into `<TABLE_NAME>`.  
`./simple_db.py select --table <TABLE_NAME>`: Reads all data from `<TABLE_NAME>`.  
`./simple_db.py select --table <TABLE_NAME> --cond <KEY>`: Reads data from `<TABLE_NAME>` with key equals `<KEY>`.  
`./simple_db.py delete --table <TABLE_NAME> --cond <KEY>`: Deletes data from `<TABLE_NAME>` with key equals `<KEY>`.  
`./simple_db.py update --table <TABLE_NAME> --data <VALUE>`: Updates all values in `<TABLE_NAME>`.  
`./simple_db.py update --table <TABLE_NAME> --cond <KEY> --data <VALUE>`: Updates value in `<TABLE_NAME>` with key equals `<KEY>`.


### Prepare development environment (valid also fon runtime)  
When in the `dbms` folder root.
1. `python3 -m venv <PATH_TO_CREATE>`  
2. `source <PATH_TO_CREATE>/bin/activate`   
3. `pip install -r requirements.txt`

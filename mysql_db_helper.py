#! python3
''' 
    Purpose: This python code will be run when running the FITS Python app.  
    Essentially, the code in this file will check for the existence of MySQL,
    the MySQL database used for FITS issue tracking, and the table(s) used in 
    said DB. 

    If MySQL does exist, but he DB/table(s) do not, this script will attempt
    to initialize them
'''

import mysql.connector

dbs = {}
dbs['issue_tracker_db'] = (
    "CREATE DATABASE issue_tracker_db2;"
)

tables = {}
tables['issues_tbl'] = (
    "CREATE TABLE issues_tbl(" +
    "  id INT(11) AUTO_INCREMENT PRIMARY KEY," +
    "  projectKey VARCHAR(100)," +
    "  title VARCHAR(200)," +
    "  description TEXT," +
    "  links TEXT," +
    "  create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
)
def checkAndMakeDB():
    db_connection = mysql.connector.connect(
        host="localhost", # replace with wherever you host your db
        user="coltan", # replace with your username
        password="qwerQWER1234!@#$" # replace with a real password
    )
    db_cursor = db_connection.cursor()

    db_cursor.execute("SHOW DATABASES;")
    databases = [item[0] for item in db_cursor.fetchall()]

    for key in dbs:
        if key in databases:
            print("Found " + key + " database!")
        else:
            print("Database " + key + " not found. Creating new database...")
            db_cursor.execute(dbs[key])
        
    # If I ever used more than one DB for some reason, would need to update
    #  hard coded values here and in the for loop below...
    db_cursor.execute("SHOW TABLES in issue_tracker_db;")

    dbTables = [item[0] for item in db_cursor.fetchall()]

    for key in tables:
        if key in dbTables:
            print("Found " + key + "!")
        else:
            print(key + " not found. Creating table...")
            db_cursor.execute("USE issue_tracker_db;")
            db_cursor.execute(tables[key])

    db_cursor.close()

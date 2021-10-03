import mysql.connector as mysql
from dotenv import dotenv_values
from mysql.connector.errors import DatabaseError, ProgrammingError

# get all .env key & values from '/.env' [create yours in root dir]
config = {**dotenv_values(".env")}
db = 'phonebook'
tables = ['Contact', 'Address']

try:
    db_config = mysql.connect(  # hover over connect
        host=config["HOST"],
        user=config["USER"],
        passwd=config["PASSWORD"],
        database=db
    )
except ProgrammingError as err:
    print(err)

# creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db_config.cursor()

# creating a databse called 'phonebook' if not exist
# 'execute()' method is used to compile a 'SQL' statement
# below statement is used to create tha 'phonebook' database
# cursor.execute("SHOW databases")
# databases = cursor.fetchall()

query_create_db = "CREATE DATABASE phonebook"
query_create_table = "CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255)"

# Try creating a table if not exist yet
try:
    cursor.execute(query_create_db)
except DatabaseError as err:
    print(err)

cursor.execute("SHOW databases")
print(cursor.fetchall())  # fetches and print the db

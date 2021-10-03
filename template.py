import mysql.connector as mysql
from dotenv import dotenv_values
from mysql.connector.errors import DatabaseError, ProgrammingError

# get all .env key & values from '/.env' [create yours in root dir]
config = {**dotenv_values(".env")}
db = 'phonebook'

try:
    db_config = mysql.connect(  # hover over connect
        host=config["HOST"],
        user=config["USER"],
        passwd=config["PASSWORD"],
        database=db
    )
    print("Connected with database:", db)
except ProgrammingError as err:
    print("Couldn't Connect")
    print(err)


# creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db_config.cursor()

# creating a databse called 'phonebook' if not exist
# 'execute()' method is used to compile a 'SQL' statement
# below statement is used to create tha 'phonebook' database
# cursor.execute("SHOW databases")
# databases = cursor.fetchall()
drop_table_query = ("DROP TABLE contact", "DROP TABLE address","DROP TABLE category")

# Drop table if exists
try:
    for q in drop_table_query:
        cursor.execute(q)
except ProgrammingError as err:
    print(err)

print("Dropped all tables")

query_create_db = "CREATE DATABASE phonebook"
query_create_table_contact = "CREATE TABLE contact (contactID INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), tel VARCHAR(20))"
query_create_table_address = "CREATE TABLE address (addressID INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY, email VARCHAR(50), country VARCHAR(25), region VARCHAR(25))"
query_create_table_category = "CREATE TABLE category (categoryID INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), description VARCHAR(255))"

db_query = (query_create_table_contact,
            query_create_table_address, query_create_table_category)


# Try creating a table if not exist yet
try:
    cursor.execute(query_create_db)
    print("db created")
except DatabaseError as err:
    print(err)

# Try creating tables
try:
    for query in db_query:
        cursor.execute(query)
        db_config.commit()
        
# to make final output we have to run the 'commit()' method of the database object, as above 
    print("Tables created")
except DatabaseError as err:
    print(err)


cursor.execute("SHOW TABLES")
print(cursor.fetchall())  # fetches and print all tables


# 'DESC table_name' is used to get all columns information
# cursor.execute("DESC contact")
# it will print all the columns as 'tuples' in a list
# print(cursor.fetchall())

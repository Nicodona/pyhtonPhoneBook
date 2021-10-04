import mysql.connector as mysql
from mysql.connector.errors import ProgrammingError
from dotenv import dotenv_values


config = {**dotenv_values(".env")}

def connect(DB_NAME = 'phonebook'):
    try:
        cnx = mysql.connect(  # hover over connect
            host=config["HOST"],
            user=config["USER"],
            passwd=config["PASSWORD"],
            database=DB_NAME
        )
        print("Connected with database:", DB_NAME)
        return cnx
    except ProgrammingError as err:
        print("Couldn't Connect")
        print(err)
        return

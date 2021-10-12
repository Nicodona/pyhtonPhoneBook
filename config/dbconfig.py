from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

config = {**dotenv_values(".env")}
DB_NAME = 'phonebook'

TABLES = {}

TABLES['contact_group'] = (
    "CREATE TABLE `contact_group` ("
    "  `groupID` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(20),"
    "  `description` varchar(20),"
    "  PRIMARY KEY (`groupID`)"
    ") ENGINE=InnoDB")

TABLES['contact'] = (
    "CREATE TABLE `contact` ("
    "  `contactID` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(20),"
    "  `tel` varchar(20),"
    "  `date_created` date,"
    "   `groupID` int(11) NOT NULL,"
    "  PRIMARY KEY (`contactID`),"
    "  CONSTRAINT `contact_ibfk_1` FOREIGN KEY (`groupID`) "
    "     REFERENCES `group` (`groupID`)"
    ") ENGINE=InnoDB")

TABLES['address'] = (
    "CREATE TABLE `address` ("
    "  `addressID` int(11) NOT NULL AUTO_INCREMENT,"
    "  `email` varchar(20),"
    "  `country` varchar(20),"
    "   `region` varchar(20),"
    "  `contactID` int(11) NOT NULL,"
    "  PRIMARY KEY (`addressID`),"
    "  CONSTRAINT `address_ibfk_1` FOREIGN KEY (`contactID`) "
    "     REFERENCES `contact` (`contactID`)"
    ") ENGINE=InnoDB")


cnx = mysql.connector.connect(
    user=config["USER"], host=config["HOST"], passwd=config["PASSWORD"])
cursor = cnx.cursor()


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()

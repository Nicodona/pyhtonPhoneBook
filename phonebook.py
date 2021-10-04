from __future__ import print_function
import config.connect

try:
    cnx = config.connect.connect(DB_NAME='phonebook')
    cursor = cnx.cursor()
except AttributeError as err:
    print(err)

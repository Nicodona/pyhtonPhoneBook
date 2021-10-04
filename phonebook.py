try:
    cnx = config.connect.connect(DB_NAME='phonebook')
    cursor = cnx.cursor()
except AttributeError as err:
    print(err)

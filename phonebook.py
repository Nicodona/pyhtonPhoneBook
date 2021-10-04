from __future__ import print_function
import config.connect

try:
    cnx = config.connect.connect(DB_NAME='phonebook')
    cursor = cnx.cursor()
except AttributeError as err:
    print(err)


class Contact:
    def __init__(self) -> None:
        print("Creating contact..")
        pass

    def create(self, name, tel, groupID):
        add_contact = ("INSERT INTO contact "
                       "(name, tel, groupID) "
                       "VALUES (%s, %s, %s)")
        data_contact = {
            'name': name,
            'tel': tel,
            'groupID': groupID
        }
        cursor.execute(add_contact, data_contact)

        # Make sure data is committed to the database
        close_connection()
        print("Contact successfuly created")
        pass

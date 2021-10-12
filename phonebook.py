from __future__ import print_function

from mysql.connector.utils import NUMERIC_TYPES
import config.connect

cnx = ''
cursor = ''


def open_connection():
    try:
        global cnx, cursor
        cnx = config.connect.connect(DB_NAME='phonebook')
        cursor = cnx.cursor()
    except AttributeError as err:
        print(err)


class PhoneBook:
    def __init__(self) -> None:
        print("Phonebook initialized... Choose operation")
        pass
    def menu(self):
        # We created this simple menu function for
        # code reusability & also for an interactive console
        # Menu func will only execute when called
        print("********************************************************************")
        print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
        print("********************************************************************")
        print("\tYou can now perform the following operations on this phonebook\n")
        print("1. Add a new contact")
        print("2. Remove an existing contact")
        print("3. Delete all contacts")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Exit phonebook")
        choice = int(input("Please enter a choice"))

        return choice


class Contact:
    def __init__(self) -> None:
        print("Processing contact....")
        pass

    def create(self, name, tel, groupID):
        open_connection()
        add_contact = ("INSERT INTO contact "
                       "(name, tel, groupID) "
                       "VALUES (%s, %s, %s)")
        data_contact = (name, tel, groupID)
        cursor.execute(add_contact, data_contact)

        # Make sure data is committed to the database
        cnx.commit()
        close_connection()
        print("Contact successfuly created")
        pass
    
    def delete(self, name:str=""):
        open_connection()
        query = ("DELETE FROM contact "
                "WHERE name=%s; ")
        cursor.execute(query, (name, ))
        cnx.commit()
        print("DELETED")
        close_connection()
        pass

    def update(self,id: int=0, name:str="", tel:str="", groupID:int=0):
        open_connection()
        query = ("UPDATE contact"
                "SET name=%s, "
                "SET tel=%s, "
                "SET groupID=%s "
                "WHERE id=%s ")
        cursor.execute(query, (name, tel, groupID, id))
        cnx.commit()
        print("Succesfully updated groudid", id)
        close_connection()
        pass

    def get_one(self, name=""):
        open_connection()
        query = ("SELECT * from contact "
                "WHERE name=%s ")
        cursor.execute(query, (name,))
        r = cursor.fetchone()
        print(r)
        close_connection()
        pass

    def get_all(self):  # return all groups
        open_connection()
        query = "SELECT * FROM contact"
        cursor.execute(query)
        result = cursor.fetchall()
        for r in result:
            print(r)
        close_connection()
        pass
      

class Address:
    def __init__(self) -> None:
        print("Processing group....")
        pass

    def create(self, email="", country="", region="",contactID=""):
        open_connection()
        add_group = ("INSERT INTO address "
                     "(email, country, region, contactID) "
                     "VALUES(%s, %s)")
        # Insert address
        d = (email, country, region, contactID)
        cursor.execute(add_group, d)
        cnx.commit()
        # Make sure data is committed to the database and close conn
        close_connection()
        print("Group successfuly created")
        return "created"

    def delete(self, email=""):
        open_connection()
        query = ("DELETE FROM address "
                "WHERE email=%s; ")
        cursor.execute(query, (email, ))
        cnx.commit()
        print("DELETED")
        close_connection()
        pass

    def update(self,id: int=0, email:str="", country="", region="", contactID:int=0):
        open_connection()
        query = ("UPDATE adress "
                "SET email=%s ,"
                "SET country=%s ,"
                "SET region=%s ,"
                "SET contactID=%s "
                "WHERE groupID=%s ")
        cursor.execute(query, (email,country,region,contactID, id))
        cnx.commit()
        print("Succesfully updated groudid", id)
        close_connection()
        pass

    def get_one(self, name=""):
        open_connection()
        query = ("SELECT * FROM address "
                "WHERE name=%s ")
        cursor.execute(query, (name,))
        r = cursor.fetchone()
        print(r)
        close_connection()
        pass

    def get_all(self):  # return all addresses
        open_connection()
        query = "SELECT * FROM address"
        cursor.execute(query)
        result = cursor.fetchall()
        for r in result:
            print(r)
        close_connection()
        pass
        

class Group:
    def __init__(self) -> None:
        print("Processing group....")
        pass

    def create(self, name, desc):
        open_connection()
        add_group = ("INSERT INTO contact_group "
                     "(name, description) "
                     "VALUES(%s, %s)")
        # Insert group information
        data_group = {
            'name': name,
            'description': desc
        }
        d = (name, desc)
        cursor.execute(add_group, d)
        cnx.commit()
        # Make sure data is committed to the database and close conn
        close_connection()
        print("Group successfuly created")
        return "created"

    def delete(self, name=""):
        open_connection()
        query = ("DELETE FROM contact_group "
                "WHERE name=%s; ")
        cursor.execute(query, (name, ))
        cnx.commit()
        print("DELETED")
        close_connection()
        pass

    def update(self,id: int=0, name:str=""):
        open_connection()
        query = ("UPDATE contact_group "
                "SET name=%s "
                "WHERE groupID=%s ")
        cursor.execute(query, (name, id))
        cnx.commit()
        print("Succesfully updated groudid", id)
        close_connection()
        pass

    def get_one(self, name=""):
        open_connection()
        query = ("SELECT name, description from contact_group "
                "WHERE name=%s ")
        cursor.execute(query, (name,))
        r = cursor.fetchone()
        print(r)
        close_connection()
        pass

    def get_all(self):  # return all groups
        open_connection()
        query = "SELECT * FROM contact_group"
        cursor.execute(query)
        result = cursor.fetchall()
        for r in result:
            print(r)
        close_connection()
        pass
        
        


def close_connection():
    cursor.close()
    cnx.close()
    pass

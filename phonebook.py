from __future__ import print_function
import config.connect

cnx = ''
cursor = ''

def connect_now():
try:
        global cnx, cursor
    cnx = config.connect.connect(DB_NAME='phonebook')
    cursor = cnx.cursor()
except AttributeError as err:
    print(err)


class PhoneBook:
    def __init__(self,):
        # other init setup. create Address object
        print("phonebook initialized")

    # create a phonebook
    def create(self):
        pass

    def edit(self):
        pass

    def update(self):
        pass

    def delete(self):
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


class Address:
    def __init__(self, email, country, region, contactID) -> None:
        pass


class Group:
    def __init__(self) -> None:
        print("Creating a group....")
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
        close_connection()
        print("Group successfuly created")
        pass

    def delete(self, id):
        pass

    def update(self,id: int=0, name=""):
        open_connection()
        query = ("UPDATE contact_group "
                "SET name=%s "
                "WHERE groupID=%s ")
        cursor.execute(query, (name, id))
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

    def get_groups(self):  # return all groups
        open_connection()
        query = "SELECT * FROM contact_group"
        cursor.execute(query)
        result = cursor.fetchall()
        for r in result:
            print(r)
        close_connection()
        pass
        
        


def close_connection():
    cnx.commit()
    cursor.close()
    cnx.close()
    pass

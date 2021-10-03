import mysql.connector as mysql

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
	def __init__(self, name, tel, groupID) -> None:
		pass

class Address:
	def __init__(self, email, country, region, contactID) -> None:
		pass

class Group:
	def __init__(self, ):
		print("something")
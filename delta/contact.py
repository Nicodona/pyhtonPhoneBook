
class PhoneBook:
	def __init__(self,name,tel,email,address):
		# other init setup. create Address object
		print("phonebook initialized")
		menu()
	def menu():
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

class Address:
	def __init__(self, city, state, zip_code):
		# init vars here


from phonebook import Group, PhoneBook

group_members = [
    {"name": "Family",
        "description": "For my family"
     },
    {"name": "Friends",
     "description": "all my Friends"
     },
    {"name": "Business",
     "description": "Business partners"
     },
]

# create groups
# group = Group()
#     for g in group_members:
#         group.create(g.get("name"), g.get("description"))
def run():
    phonebook = PhoneBook()
    # add=1, rmv=2, update=3, get=4,getall=5, exit=6
    while True:
        phonebook.menu()
        if(phonebook.menu==1):
            phonebook.create()
        if(phonebook.menu==2):
            phonebook.delete()
        if(phonebook.menu==3):
            phonebook.update()
        if(phonebook.menu==4):
            phonebook.get_one()
        if(phonebook.menu==5):
            phonebook.get_all()
        elif(phonebook.menu==6):
            print("Thanks for using our application")
            break
        
        

    print("app exited:>0")

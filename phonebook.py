import re

namepat = re.compile(r"[A-Za-z]+\s+[A-Za-z]+\s+[A-Za-z]+")
phonepat = re.compile(r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")

contacts = {}

def add():
    name = input('Enter name : ')
    if re.fullmatch(namepat,name):
        number = input("Enter the phone number : ")
        if re.fullmatch(phonepat,number):
            contacts[name] = number
            print('Contact added')
        else:
            print("WARNING..!\nPhone number should be numbers\nIndian phone numbers only accepted")
    else:
        print("WARNING..!\nName should be alphabets")
    #pass
def sortList():
    if len(contacts) > 0:
        print('CONTACT LIST')
        names = list(contacts.keys())
        names.sort()
        for name in names:
            print(f'Name : {name}')
            print(f'Number : {contacts[name]}')
    else:
        print('No contacts')
def delete():
    name = input("Enter the name to delete contact : ")
    if re.fullmatch(namepat, name):
        if contacts.get(name):
            del contacts[name]
            print(f'The contact of {name} was deleted')
        else:
            print(f'{name} does not exist')
    else:
        print('Name should be in alphabets only')

def searchNum():
    n = input('Enter phone number to search : ')
    if re.fullmatch(phonepat,n):
        for name,number in contacts.items():
            if number==n:
                print(f"Name : {name}")
                print(f"Number : {number}")
                return
        print(f"{n} does not exist")
    else:
        print("Phone number should be in digits only\nIt should be an Indian phone number")

def searchName():
    n = input("Enter name to search : ")
    if re.fullmatch(namepat, n):
        for name,number in contacts.items():
            if name.lower() == n.lower():
                print(f'Name : {name}')
                print(f'Number : {number}')
                return
        print(f'{n} does not exist')
    else:
        print('Name should be in alphabets only')

while(True):
    print('''
    1.List all contacts
    2.Add new contact
    3.Delete a contact
    4.Search by name
    5.Search by number
    6.Exit''')
    usr = input("Enter your option : ")
    if usr.isdigit():
        opt = int(usr)
        match opt:
            case 1: sortList()
            case 2: add()
            case 3: delete()
            case 4: searchName()
            case 5: searchNum()
            case 6: break
            case _: print('Invalid range. Please choose between (1 to 6)')
    else:
        print("Albhabets, negative numbers, white spaces and special characters will not be accepted as option")

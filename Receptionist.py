import re
import datetime

namepat = re.compile(r"^[A-Za-z][A-Za-z\s]{1,30}[A-Za-z]$")
phonepat = re.compile(r"^(\+91[\-\s]?)?0?(91)?[789]\d{9}$")
agepat = re.compile(r"^[1-9]+[0-9]+")
placepat = re.compile(r"[A-Za-z]{4,}$")
patients = {}
department = ['General','Ortho','Ent','Neuro','Nephro','Ophthalmo','Dental']
id = 100
token = 0
def createPat():
    try:
        global id
        name = input("Enter Patient Name : ")
        if re.fullmatch(namepat,name):
            name = name.title()
            age = input("Enter the age : ")
            if re.fullmatch(agepat,age):
                age = int(age)
                place = input("Enter the place : ")
                if re.fullmatch(placepat,place):
                    place = place.title()
                    phone = input("Enter the phone number : ")
                    if re.fullmatch(phonepat,phone):
                        dep = input(f"Available departments : {department}\nEnter the department : ")
                        dep = dep.title()
                        if dep in department:
                            x = datetime.datetime.now()
                            id += 1
                            patients[id] = {'name': name,'age':age,'place':place,'phone':phone,'dep':dep,'date':x.strftime("%c")}
                            print("New Patient Added Successfully")
                        else:
                            print("This department does not exist in our hospital")
                    else:
                        print("WARNING..!\nPhone number should be numbers\nIndian phone numbers only accepted")
                else:
                    print("Wrong input at place. Verify and try again")
            else:
                print("Invalid entry. Enter age correctly")
        else:
            print("Invalid Name")

    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(e)
    return

def updatePat():
    try:
        id1 = int(input("Enter patient id to be modified : "))
        if id1 < 0:
            raise Exception("ID cannot be negative")
        elif id1 < 101:
            raise Exception("ID starts from '101'")
        elif id1 not in patients.keys():
            raise Exception("ID does not existing")
        else:
            inp = input("Enter what to be modified\nn : for name\na : for age\np : for place\nph : for phone\nd : for department\nEnter your choice : ")
            if inp == 'n':
                name = input("Enter correct name : ")
                if re.fullmatch(namepat,name):
                    name = name.title()
                    patients[id1]['name'] = name
                    print("Patient name has been updated")
                else:
                    print("Invalid Name")
            elif inp == 'a':
                age = input("Enter correct age : ")
                if re.fullmatch(agepat,age):
                    patients[id1]['age'] = age
                    print("Patient's age updated successfully")
                else:
                    print("Invalid entry. Enter age correctly")
            elif inp == 'p':
                place = input("Enter correct place : ")
                if re.fullmatch(placepat,place):
                    place = place.title()
                    patients[id1]['place'] = place
                    print("Patient's place has been updated")
                else:
                    print("Wrong input at place. Verify and try again")
            elif inp == 'ph':
                phone = input("Enter correct phone number : ")
                if re.fullmatch(phonepat,phone):
                    patients[id1]['phone'] = phone
                    print("Patient's phone number updated successfully")
                else:
                    print("WARNING..!\nPhone number should be numbers\nIndian phone numbers only accepted")
            elif inp == 'd':
                dep = input(f"Available departments : {department}\nUpdate department : ")
                dep = dep.title()
                if dep in department:
                    patients[id1]['dep'] = dep
                    print("Department updated successfully")
                else:
                    print("This department does not exist in our hospital")
            else:
                print("Invalid choice")
            x = datetime.datetime.now()
            patients[id1]['date'] = x.strftime("%c")
    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(e)
    return

def deletePat():
    try:
        id1 = int(input("Enter patient id to be deleted : "))
        if id1 < 0:
            raise Exception("ID cannot be negative")
        elif id1 < 101:
            raise Exception("ID starts from '101'")
        elif id1 not in patients.keys():
            raise Exception("ID does not existing")
        else:
            del patients[id1]
            print("Patient deleted")
    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(e)
    return

def searchPat():
    try:
        id1 = int(input("Enter Patient ID : "))
        if id1 < 0:
            raise Exception("ID cannot be negative")
        elif id1 < 101:
            raise Exception("ID starts from '101'")
        elif id1 not in patients.keys():
            raise Exception("ID does not existing")
        else:
            print("Patient Record : ",patients.get(id1))
    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(e)
    return

def listPat():
    if not patients:
        print("Patient database is empty")
    else:
        print("All Patient Records With Last Updated Date & Time\n")
        for x in range(101,id + 1):
            i = patients.get(x)
            print(f"Patient ID : {x} {i}\n")

def tokenGenerate():
    try:
        global token
        id1 = int(input("Enter patient id : "))
        if id1 < 0:
            raise Exception("ID cannot be negative")
        elif id1 < 101:
            raise Exception("ID starts from '101'")
        elif id1 not in patients.keys():
            raise Exception("ID does not existing")
        else:
            token += 1
            x = datetime.datetime.now()
            print(f"Name : {patients[id1]['name']}\nToken no : {token}\nAppoinment date : ",x.strftime("%c"))
    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(e)
    return

database = {'RECEPTION':'1234'}
usrnm = input("Enter the username : ")
if usrnm == list(database.keys())[0]:
    password = input("Enter the password : ")
    if password == database[usrnm]:
        print("WELCOME TO ",usrnm)
        while True:
            ch = input('''Patients are waiting....
                    1.New Patient
                    2.Update Patient
                    3.Delete Patient
                    4.Search Patient
                    5.List of Patients
                    6.Token
                    7.Exit
                    Enter your choice : ''')
            if ch.isdigit():
                ch = int(ch)
                if ch == 1:
                    createPat()
                elif ch == 2:
                    updatePat()
                elif ch == 3:
                    deletePat()
                elif ch == 4:
                    searchPat()
                elif ch == 5:
                    listPat()
                elif ch == 6:
                    tokenGenerate()
                elif ch == 7:
                    exit('  Thank You.\nSee You Again..!')
                else:
                    print("Invalid range, please enter between 1 to 7")
            else:
                print("Invalid option")
    else:
        print("You are not authorized")
else:
    print("Invalid Username")

#this class defines all the main functions of the program
import db
from passwords import passwords

#this function gets the password of an existing service in db
def getPassword(p1):
    service = input("Enter a service to get it's password: ").lower()
    password = db.get_Password(service)

    if(password is None):
        print("The service, " + service + "doesn't exist. Create the service and store a password")
    else:
        password = p1.decryptServicePassword(password)
        print("The password for the service, " + service + " is: " + password)

#stores the service and generates a random password for it
def storePassword(p1):
    service = input("Enter a service to save its password: ").lower()
    randomPW = p1.createRandomPassword()
    encryptedeRandomPW = p1.encryptServicePassword(randomPW)
    queryResult = db.store_Password(service, encryptedeRandomPW)

    if(queryResult is not None):
        print("The service, " + service + " was saved. Its password is: " + randomPW)
    else:
        print("The service, " + service + " already exists. Enter a new service.")

#updates an existing services password by generating new random password
def updatePassword(p1):
    return None

#changes the master password if its correct
def changeMasterPassword(p1):
    return None


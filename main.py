#this class defines all the main functions of the program
import db
from passwords import passwords

#this function gets the password of an existing service in db
def getPassword(p1):
    service = input("Enter a service to get it's password: ").lower()
    password = db.get_Password(service)

    if(password is None):
        print("The service, " + service + " doesn't exist. Create the service and store a password")
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
        print("The service, " + service + " was saved. Its password is: " + p1.decryptServicePassword(encryptedeRandomPW))
    else:
        print("The service, " + service + " already exists. Enter a new service.")

#updates an existing services password by generating new random password
def updatePassword(p1):
    service = input("Enter a service to update its password: ").lower()
    randomPW = p1.createRandomPassword()
    encryptedeRandomPW = p1.encryptServicePassword(randomPW)
    queryResult = db.update_Password(service, encryptedeRandomPW)
    if(queryResult is not None):
        print(randomPW)
        print("The service " + service + " password was updated. The updated password is " + p1.decryptServicePassword(encryptedeRandomPW))
    else:
        print("The service " + service + " does not exist. Either create a new service or update a different service.")

#changes the master password if its correct
def changeMasterPassword(p1):
    yourMasterPassword = input("Enter your current Master password to change it: ")
    actualMasterPassoword = db.get_MasterPassword()

    if(VerifyMasterPassword(p1,yourMasterPassword,actualMasterPassoword)):
        newPW = input("Enter a new password: ")
        p1 = passwords(newPW)
        db.update_Master_Password(p1.hashedPassword)
        print("The Master password you entered, " + newPW + " was saved as your new Master password.")

#verifys if the master password is correct or not
def VerifyMasterPassword(p1,yourMasterPassword,actualMasterPassword):
    if (p1.isCorrectHash(yourMasterPassword.encode(), actualMasterPassword)):
        print("The master password is correct")
        return True
    else:
        print("The master password is not correct. Try again")
        return False

#creates a master password by adding it to db
def CreateMasterPassword(p1):
    db.store_Master_Password(p1.hashedPassword)
    print("No previous Master password was found. The master password you entered has been saved as your new master password")



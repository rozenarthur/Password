#this file runs all the main methods, acts as driver
import db
from passwords import passwords

db.create_Table()
db.create_Master_Table()

flag = True
while (flag is True):
    yourMasterPassword = input("Enter your master password to access all your service passwords: ")
    actualMasterPassword = db.get_MasterPassword()
    p1 = passwords(yourMasterPassword)

    if(actualMasterPassword is None):
        print(db.store_Master_Password(p1.hashedPassword))
        actualMasterPassword = p1.hashedPassword
        print("No previous Master password was found. The master password you entered has been saved as your new master password")

    else:
        if(p1.isCorrectHash(yourMasterPassword, actualMasterPassword)):
            flag = False
            print("The master password is correct")
        else:
            print("The master password is not correct. Try again")






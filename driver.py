#this file runs all the main methods, acts as driver
import db
import main
from passwords import passwords

db.create_Table()
db.create_Master_Table()

actualMasterPassword = db.get_MasterPassword()
p1 = passwords('')

flag = True
while (flag is True):
    yourMasterPassword = input("Enter your master password to access all your service passwords: ")
    actualMasterPassword = db.get_MasterPassword()
    p1 = passwords(yourMasterPassword)

    if(actualMasterPassword is None):
        db.store_Master_Password(p1.hashedPassword)
        actualMasterPassword = p1.hashedPassword
        print("No previous Master password was found. The master password you entered has been saved as your new master password")

    else:
        if(p1.isCorrectHash(yourMasterPassword.encode(), actualMasterPassword)):
            flag = False
            print("The master password is correct")
        else:
            print("The master password is not correct. Try again")

flag2 = True
while(flag2 is True):
    instruction = input("""
    ***************************
    Instructions:
    gp = get Password
    sp = store Password
    up = update Password
    cp = change master Password
    q = quit Program
    ***************************   
    """)

    if(instruction.lower() == 'gp'):
        main.getPassword(p1)
    elif(instruction.lower() == 'sp'):
        main.storePassword(p1)
    elif (instruction.lower() == 'up'):
        main.updatePassword(p1)
    elif(instruction.lower() == 'cp'):
        main.changeMasterPassword(p1)
    elif(instruction.lower() == 'q'):
        flag2 = False
    else:
        print("You entered an invalid command. Try again!")


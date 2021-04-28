#this file runs all the main methods, acts as driver
import db
import main
from passwords import passwords

db.create_Table()
db.create_Master_Table()

actualMasterPassword = db.get_MasterPassword()
p1 = passwords('')

flag = False
while (flag is False):
    yourMasterPassword = input("Enter your master password to access all your service passwords: ")
    actualMasterPassword = db.get_MasterPassword()
    p1 = passwords(yourMasterPassword)

    if(actualMasterPassword is None):
        main.CreateMasterPassword(p1)
        actualMasterPassword = p1.hashedPassword
    else:
        flag = main.VerifyMasterPassword(p1,yourMasterPassword,actualMasterPassword)

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
        db.close_db()
    else:
        print("You entered an invalid command. Try again!")
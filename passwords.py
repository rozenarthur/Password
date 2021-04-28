# this file will handle all the encryption, decryption, and hashing of the master password and service passwords
import bcrypt #hashed password for master password
from cryptography.fernet import Fernet #encryption for service password
import random
import string

# constructor for getting the hashed master password
class passwords:
    def __init__(self, masterPassword):
        self.hashedPassword = bcrypt.hashpw(masterPassword.encode(), bcrypt.gensalt())
        self.key = Fernet.generate_key()

    #checks if the hashed password is correct
    def isCorrectHash(self, password, hashedPassword):
        if(bcrypt.checkpw(password, hashedPassword)):
            return True
        else:
            return False

    #encrypts the service password and a returns the encrypted password
    def encryptServicePassword(self, password = ''):
        encodedPassword = password.encode()
        fernetKey = Fernet(self.key)
        return fernetKey.encrypt(encodedPassword)

    #decrypts the hashed service password and returns the decrypted service password
    def decryptServicePassword(self, hashedPassword = ''):
        fernetKey = Fernet(self.key)
        return fernetKey.decrypt(hashedPassword).decode()

    #creates a random password of characters from 8 to 20 characters
    def createRandomPassword(self):
        specialchar = '!@#$%^&*,.:?'
        passwordLength = random.randrange(8,20)
        randomPassword = ''
        i = 0
        for i in range(passwordLength):
            randchar = random.choice(string.ascii_letters + string.digits + specialchar)
            randomPassword += randchar
        return randomPassword
# this file performs common sql commands to create, store and update the database of services and passowords
import sqlite3
import config

#the settings to connect to the DataBase
connect = sqlite3.connect(config.DBName)
c = connect.cursor()
passwordTableName = "Passwords"
masterPasswordTableName = "Master_Password"

#Creates the initial table of passwords
def create_Table():
    c.execute("CREATE TABLE IF NOT EXISTS " + passwordTableName + " (ServiceName PRIMARY KEY, Password TEXT)")

#inserts the service and the password into the database - only works when service doesn't exist
def store_Password(service, password):
    try:
        c.execute("INSERT INTO " + passwordTableName + " VALUES (?, ?)", (service, password))
        connect.commit()
        return "The password " + password + " was saved for the service " + service
    except:
        return "The service " + service + " already exists. Enter a new service or get a new password for existing service."

#updates an existing service, with a new password
def update_Password(service, password):
    try:
        c.execute("UPDATE " + passwordTableName + " SET Password = ? WHERE ServiceName = ?", (password, service))
        connect.commit()
        return "The password" + password + " was updated for the service " + service
    except:
        return "The service " + service + " does not exist. Either create a new service or update a different service."

#gets returns the password of the service
def get_Password(service):
    try:
        return c.execute("SELECT Password FROM " + passwordTableName + " WHERE ServiceName = ? ", (service,)).fetchone()[0]
    except:
        return None

#Creates a table for the master password
def create_Master_Table():
    c.execute("CREATE TABLE IF NOT EXISTS " + masterPasswordTableName + " (MasterPassword TEXT, Password TEXT)")

#creates an initial master password
def store_Master_Password(password):
    try:
        c.execute("INSERT INTO " + masterPasswordTableName + " VALUES ('MasterPassword', ?)", (password,))
        connect.commit()
        return "Your master password was saved"
    except:
        return "An existing master password already exists. You need to change the master password"

#gets returns the master password of the user
def get_MasterPassword():
    try:
        return c.execute("SELECT Password FROM " + masterPasswordTableName + " WHERE MasterPassword = 'MasterPassword' ").fetchone()[0]
    except:
        return None

#updates the existing master password
def update_Master_Password(password):
    try:
        c.execute("UPDATE " + passwordTableName + " SET Password = ? WHERE MasterPassword = MasterPassword", (password,))
        connect.commit()
        return "The master password was updated"
    except:
        return "No master password currently exists. First create a master password before changing it"

def close_db():
    c.close()
    connect.close()

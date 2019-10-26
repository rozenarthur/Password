# this file performs common sql commands to create, store and update the database of services and passowords
import sqlite3
import config

#the settings to connect to the DataBase
connect = sqlite3.connect(config.DBName)
c = connect.cursor()
passwordTableName = "Passwords"
masterPasswordTableName = "Master Password"

#Creates the initial table of passwords
def create_Table():
    c.execute("CREATE TABLE IF NOT EXISTS " + passwordTableName + " (ServiceName PRIMARY KEY, Password TEXT)")

#inserts the service and the password into the database - only works when service doesn't exist
def store_Password(service ,password):
    c.execute("INSERT INTO " + passwordTableName + " VALUES (?, ?)", (service, password))
    connect.commit()

#gets returns the password of the service
def get_Password(service):
    return c.execute("SELECT Password FROM " + passwordTableName + " WHERE ServiceName = ? ", (service,)).fetchone()[0]

def close_db():
    c.close()
    connect.close()


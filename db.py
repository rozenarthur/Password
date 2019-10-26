# this file performs common sql commands to create, store and update the database of services and passowords
import sqlite3
import config

#the settings to connect to the DataBase
connect = sqlite3.connect(config.DBName)
c = connect.cursor()
TableName = config.TableName

#Creates the initial table of passwords
def create_Table():
    c.execute("CREATE TABLE IF NOT EXISTS " + TableName + "(ServiceName TEXT, Password TEXT)")

#inserts the service and the password into the database
def store_Password(service ,password):
    isServiceFound = c.execute("SELECT * FROM " + TableName + " WHERE ServiceName=" + service).rowcount

    #only store the password if the service doesn't exist
    if(isServiceFound == 0):
        c.execute("INSERT INTO " + TableName + " VALUES ('" + service + "', '" + password + "')")

    connect.commit()
    c.close()
    connect.close()

def get_Password(service):
    return c.execute("SELECT Password FROM " + TableName + " WHERE ServiceName=" + service).fetchone()
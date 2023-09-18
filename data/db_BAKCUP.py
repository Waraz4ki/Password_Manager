import sqlite3


connection = sqlite3.connect("DATABASE")
cursor = connection.cursor()
cursor.execute(""" CREATE TABLE s(Title text, Name text, Password text)""")

#! DON'T USE F STRINGS FOR THIS STUFF
#! SQL INJECTIONS WILL COME FOR YOU

def insert_entry(sth, Title, Name, Password):
    with connection:
        cursor.execute("INSERT INTO " + sth + " VALUES (:Title, :Name, :Password)", 
                       {'Title': Title, 'Name': Name, 'Password': Password})
        
def get_entry_by_title(sth, Title):
    with connection:
        cursor.execute("SELECT * FROM " + sth + " WHERE Title=:Title", 
                       {'Title':Title})
        print(cursor.fetchone())
        return cursor.fetchone()
        
def get_eveything(sth):
    with connection:
        cursor.execute("SELECT * FROM " + sth)
        print(cursor.fetchall())
        return cursor.fetchall()

#!Doesn't quit work
def update_entry(sth, Title, Name, Password):
    with connection:
        cursor.execute("UPDATE " + sth + " SET Title=:Title, Name=:Name, Password=:Password WHERE Title=:Title AND Name=:Name", 
                       {'Title': Title, 'Name': Name, 'Password': Password})

def delete_entry(sth, Title, Name):
    with connection:
        cursor.execute("DELETE from "+ sth + " WHERE Title=:Title AND Name=:Name",
                       {'Title': Title, 'Name': Name})

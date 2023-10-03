import sqlite3
import hashlib
import secrets

#! Switch to MYSQL someday

class DBClass:
    def __init__(self, DATABASE):
        self.DATABASE= DATABASE
        self.connection = sqlite3.connect(DATABASE)
        self.cursor = self.connection.cursor()

    
    def firstSetup(self, masterKEY):
        data=[masterKEY]
        with self.connection:
            self.cursor.execute("CREATE TABLE Config (masterKEY)")
            self.cursor.execute("INSERT INTO Config VALUES (?)", data)
            self.connection.commit()
            self.cursor.execute("CREATE TABLE test12(Title text, Name text, Password text, Notes text)")

    def openingCheck(self):
        with self.connection:
            res = self.cursor.execute("SELECT masterKEY FROM Config")
            return res.fetchone()[0]
        
    def insert_entry(self, Title, Name, Password, Notes):
        with self.connection:
            self.cursor.execute("INSERT INTO " + self.DATABASE + " VALUES (:Title, :Name, :Password, :Notes)", 
                                {'Title': Title, 'Name': Name, 'Password': Password, 'Notes': Notes})
    
    def update_entry(self, Title, Name, Password):
        with self.connection:
            self.cursor.execute("UPDATE " + self.DATABASE + "SET",
                                {})
    
    def delete_entry(self, Title, Name):
        with self.connection:
            self.cursor.execute("DELETE from " + self.DATABASE + " WHERE Title=:Title AND Name=:Name",
                                {'Title': Title, 'Name': Name})

    def get_entry_by_title(self, Title):
        with self.connection:
            self.cursor.execute("SELECT * FROM " + self.DATABASE + " WHERE Title=:Title", 
                                {'Title': Title})
            return self.cursor.fetchall()
    
    def get_every_entry(self):
        with self.connection:
            self.cursor.execute("SELECT * FROM " + self.DATABASE)
            print(self.cursor.fetchall())
            return self.cursor.fetchall()

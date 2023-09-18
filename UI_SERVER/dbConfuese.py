import sqlite3
import hashlib
import secrets


class DB:
    def __init__(self, DATABASE):
        self.connection = sqlite3.connect(DATABASE)
        self.cursor = self.connection.cursor()
        self.DATABASE=DATABASE
    
    def firstSetup(self):
        self.cursor.execute("CREATE TABLE " + self.DATABASE + "(Title text, Name text, Password text, Notes text)")
    
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
            self.cursor.execute("DELETE from "+ self.DATABASE + " WHERE Title=:Title AND Name=:Name",
                                {'Title': Title, 'Name': Name})

    def get_entry_by_title(self, Title):
        with self.connection:
            self.cursor.execute("SELECT * FROM " + self.DATABASE + " WHERE Title=:Title", 
                                {'Title':Title})
            return self.cursor.fetchall()
    
    def get_every_entry(self):
        with self.connection:
            self.cursor.execute("SELECT * FROM "+ self.DATABASE)
            print(self.cursor.fetchall())
            return self.cursor.fetchall()

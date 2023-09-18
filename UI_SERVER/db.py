import sqlite3
import secrets

class DBDatabase:
#! DON'T USE F STRINGS FOR THIS STUFF
#! SQL INJECTIONS WILL COME FOR YOU
    def __init__(self, Database, Table):
        self.Table = Table
        self.connection = sqlite3.connect(Database)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE " + Table + "(Title text, Name text, Password text)")

    def insert_entry(self, Title, Name, Password):
        with self.connection:
            self.cursor.execute("INSERT INTO " + self.Table + " VALUES (:Title, :Name, :Password)", 
                                {'Title': Title, 'Name': Name, 'Password': Password})

    def get_entry_by_title(self, Title, Name, Password):
        with self.connection:
            self.cursor.execute("SELECT * FROM " + self.Table + " WHERE Title=:Title", 
                                {'Title':Title})
            print(self.cursor.fetchone())
            return self.cursor.fetchone()
            
    def get_entry(self, Title, Name, Password):
        with self.connection:
            self.cursor.execute("SELECT * FROM " + self.Table)
            print(self.cursor.fetchall())
            return self.cursor.fetchall()

    #!Doesn't quit work
    def update_entry(self, Title, Name, Password):
        with self.connection:
            self.cursor.execute("UPDATE " + self.Table + " SET Title=:Title, Name=:Name, Password=:Password WHERE Title=:Title AND Name=:Name", 
                        {'Title': Title, 'Name': Name, 'Password': Password})

    def delete_entry(self, Title, Name, Password):
        with self.connection:
            self.cursor.execute("DELETE from "+ self.Table + " WHERE Title=:Title AND Name=:Name",
                        {'Title': Title, 'Name': Name})

            
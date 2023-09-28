import dbtest
import sqlite3

DB = dbtest.DBClass()

DB.firstSetup("1234")
DB.openingCheck("1234")



#con = sqlite3.connect("tutorial.db")
#cur = con.cursor()
#cur.execute("CREATE TABLE movie(title, year, score)")

#cur.execute("""
#    INSERT INTO movie VALUES
#        ('Monty Python and the Holy Grail', 1975, 8.2),
#        ('And Now for Something Completely Different', 1971, 7.5)
#""")
#con.commit()
#res = cur.execute("SELECT score FROM movie")
#print(res.fetchall())

#DB = db.DBClass(DATABASE="Das")
#res = DB.openingCheck("1234")
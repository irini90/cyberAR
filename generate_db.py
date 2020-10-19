import sqlite3, os

print("Erasing DB...")

db="database.db"

if os.path.isfile(db) :
    os.remove(db)
    con=sqlite3.connect("database.db", isolation_level=None)
    cur=con.cursor()
    print("Database deleted")
else:
    con=sqlite3.connect("database.db", isolation_level=None)
    cur=con.cursor()

f=open("dump.sql", "r")
c=f.read()
cur.executescript(c)

con.close()

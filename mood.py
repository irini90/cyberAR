import os, sqlite3, time, random
con=sqlite3.connect("database.db", isolation_level=None)
cur=con.cursor()



nar = """ <size=50><b> Timer & Mood Test </b></size=50>

    This is shit 
    """

cur.execute("update Narration set Content = ? , Help = '', Mood = ?, Alert = '', URI = ''", (nar, 1))

clock = True
count = 0

while clock == True:
   count = count + 1
   time.sleep(1)
   cur.execute("update Timer set Value = ?, Countdown = ?, Activ = ?", (count, 0, 0))

clock = False




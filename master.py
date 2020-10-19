import os, sqlite3, time, random, sys
con=sqlite3.connect("database.db", isolation_level=None)
cur=con.cursor()


 


def select():
    q= " Welcome to CybAR. Please select a scenario: "
    print("Q1", q)
    a= ['Healthcare', 'Manufacturing', 'Univeristy' ]
    cur.execute("update Narration set Content = ''")
    cur.execute("delete from Questions")
    cur.execute("insert into Questions (ID, Content) values (1, ?)", (q,))
    cur.execute("delete from Answers")
    for i in a:
        cur.execute("insert into Answers (ID, Content, Question_ID) values (?,?,1)", (a.index(i) +1,i))
    return

def answer_monitor():
    while True:
        cur.execute("select Answer_ID from User;")
        r = cur.fetchone()
        if r[0] == 0:
            time.sleep(1)
        elif r[0] != 0 and isinstance(r[0], int) :
            cur.execute("update User set Answer_ID = 0, Choice = 0") #reset answers
            cur.execute("delete from Answers")
            cur.execute("update Questions set Content = '' ")
            global c
            c= r[0]
            return

def reset():
    c="""delete from Connections ; Update Answers set Content = '' ; update Items set Skin_color = 0 , Text_placeholder_1 = '' ,
    Text_placeholder_2 = '' , Text_placeholder_3 = '', State = 'Secure' ; delete from Narration ;
    Insert into Narration Values('','',0,'',NULL) ; delete from Questions ; Insert into Questions VALUES(1,'') ;
    Update User_satisfaction set Value = 100 ; Update Timer set Value = 0 """
    cur.executescript(c)
    return


def main():
    reset()
    select()
    answer_monitor()

    if c == 1:
        os.system('python healthcare.py')

    if c == 2:
        os.system('python manufacturing.py')

    if c == 3:
        os.system('python ransom.py')
    reset()



main()










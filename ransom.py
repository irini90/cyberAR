# last edited by I 11:00
import os, sqlite3, time, random
con=sqlite3.connect("database.db", isolation_level=None)
cur=con.cursor()

p0 = 13
stageID=2
#infctable device types': 4,13,15,19,35
#cell phone, Ipad, Laptop, desktop cpu,server 

start_time = 0
end_time = 0

def start():
    q = """ This is a demonstration of a Ransomware attack in a University environment. As the attack progresses you can observe how the machines will be affected by changing colour. 
    
    Press the button to start the experience!"""
    a= ['START']
    cur.execute("update Narration set Content = ''")
    cur.execute("delete from Questions")
    cur.execute("insert into Questions (ID, Content) values (1, ?)", (q,))
    cur.execute("delete from Answers")
    for i in a:
        cur.execute("insert into Answers (ID, Content, Question_ID) values (?,?,1)", (a.index(i) +1,i))
    return

def bit1():
    nar = """ Beginning of the Attack

    A student studying in the school’s labs using his own laptop downloads a seemingly benign software, ZipTool, whilst connected to the University’s network. They install it on their machine. 
    
    Zoom in to Queen's building to observe how the attack will play out!
    """
    print(1,nar)
    cur.execute("update Narration set Content = ?", (nar,)) # if sure no duplicates just update
    time.sleep(8)
    return

def bit2():
    time.sleep(3)
    nar = """Possible threat detected!
    
    The ZipTool functions as normal from the user’s perspective, but behind the scenes communicates with servers located in different countries.
    """
    cur.execute("update Narration set Alert = ? , Content = ''", (nar,))
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID=?", (p0,))
    time.sleep(8)
    return

def bit3():
    nar="""Malware starts to perform reconnaissance! 
    
    It is now looking to identify nearby vulnerable machines in order to infect them. 
    """
    print(3, nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    nar2="""Have a closer look at the machines in the building. If the malware successfully infects a machine, its color will turn orange. 

    The dotted lines, represent the connections between the different machines. 
    
    Look out for some suspicious connections that may appear due to the malware! """
    cur.execute("update Narration set Content = ?", (nar2,))

    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID=?", (p0,))
    time.sleep(5)
    #desktops=[14, 15, 16, 17, 18, 19, 20] #lab
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  14, 1, 0) ", (p0,))
    time.sleep(2)
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID = 14")
    time.sleep(3)
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  15, 1, 0) ", (p0,))
    time.sleep(2)
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  16, 1, 0) ", (p0,))
    time.sleep(3)
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID = 16")
    time.sleep(3)
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  17, 1, 0) ", (p0,))
    time.sleep(2)
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  18, 1, 0) ", (p0,))
    time.sleep(2)
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  19, 1, 0) ", (p0,))
    time.sleep(2)
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  20, 1, 0) ", (p0,))   
    time.sleep(2)
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  5, 1, 0) ", (p0,))
    time.sleep(3)
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (5,  2, 1, 1) ")
    time.sleep(3)
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID = 2")
    time.sleep(8)
    return

def bit4():
    nar= """ Malware is now activated!
    
    The adversary has now issued the kill command, which activates the malware on the infected machine. 
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))

    nar2="""The compromised machines will now turn red.
    

    We need to take action!"""
    cur.execute("update Narration set Content = ?", (nar2,))
    cur.execute("select ID from Items where Skin_color = 1")
    infect = list(map(lambda x: x[0],cur.fetchall()))
    for i in infect:
        cur.execute("update Items set Skin_color = 2 where ID = ? ", (i,))
    time.sleep(7)
    return

def q1():
    q= "How would you like to respond?"
    print("Q1", q)
    a= ['Lockdown all network drives', 'Prevent users from making more than 50 writes to the same file in their online drives', 'Ask all infected users to bring their machines in', 'Run scenario again with AI automated cyber defense']
    cur.execute("update Narration set Content = ''")
    cur.execute("delete from Questions")
    cur.execute("insert into Questions (ID, Content) values (1, ?)", (q,))
    cur.execute("delete from Answers")
    for i in a:
        cur.execute("insert into Answers (ID, Content, Question_ID) values (?,?,1)", (a.index(i) +1,i))
    return

def a1():
    nar = """ Lockdown all network devices
    
    This will help slowing down the malware propagation, but it is too disruptive and will result in extremely frustrated 
    and angry students/lecturers, as many essential files are no longer accessible. 
    
    
    User satisfaction drops. 
    """
    print("a1",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    satisfaction(-33)
    time.sleep(12)
    return


def a2():
    nar=""" Limit Write Access
    
    This will limit the write-access, which will slow down the ransomware. """
    print("a2",nar)
    #cymian display folder icon ? infected cpus never went red ?
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(9)
    return


def a3():
    nar = """Ask staff and students to bring their machines in

    This is too slow, by the time students bring their machines in, it will be too late.
    
    What should we do next?
    """
    print("a3",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(5)
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  33, 1, 0) ", (p0,))
    time.sleep(2)
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID = 33")
    cur.execute("select Item_ID from Runtime inner join Items on Items.ID = Runtime.Item_ID where Room_ID not in (2,3) and Items.Item_type_ID in (4,13,15,19,35) and Skin_color = 0 and Building_ID = 1 order by random() limit 5")
    infect=list(map(lambda x: x[0],cur.fetchall()))
    cur.execute("select ID from Items inner join Runtime on Runtime.Item_ID = Items.ID where Skin_color = 1 and Building_ID = 1 order by random() limit 1")
    l=cur.fetchone()[0] # take a random infected machine to initiate infections
    for i in infect:
        cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?, ?, 1, 1)", (l, i)) #display connection attempts
        time.sleep(2)
        cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID =? ", (i,))
    time.sleep(8)
    return

def a4():
    nar="""AI automated defence kicks in """# then print alert about detecting early stages of ransomware
    print("a4",nar)
    cur.execute("select ID from Items where Skin_color = 1")
    infect = list(map(lambda x: x[0],cur.fetchall()))
    for i in infect:
        cur.execute("update Items set Skin_color = 0 where ID = ?", (i,))
        time.sleep(1)   
    cur.execute("update Connections set Active = 0")
    time.sleep(8)
    return

def q2():
    q= "To start the malware removal process, select an appropriate course of action."
    print("Q2", q)
    a=['Block students from downloading ZipTool', 'Ask all user’s to change their passwords', 'Take a hash of the infected file and send it to Antiviruses of infected machines', 'Disconnect the internet']
#    cur.execute("update Items set Icon='folder.xyz' where Skin_color = 1 or Skin_color = 'red.xyz'")
    cur.execute("update Narration set Content = ''")
    cur.execute("delete from Questions")
    cur.execute("insert into Questions (ID, Content) values (2, ?)", (q,))
    for i in a:
        cur.execute("insert into Answers (ID, Content, Question_ID) values (?,?,2)", (a.index(i) +1,i))
    return

def a5():
    nar=""" The ZipTool is now blocked 
    
    Not a bad choice but this does not help much since only one student (that we know of) downloaded the tool! 
    
    The remainder of the spreading occurred through network connections. Additionally, this doesn’t get rid of the malware on the already infected machines.

    What should we do next?
    """
    print("a5",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(4)
    # ipad id 28 - 32
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  28, 1, 0) ", (p0,))
    time.sleep(2)
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID = 28")
    time.sleep(3)
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  28, 0, 0) ", (p0,))
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  30, 1, 0) ", (p0,))
    time.sleep(2)
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID = 30")  
    time.sleep(3)
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  30, 0, 0) ", (p0,))
    time.sleep(6)
    return
    

def a6():
    nar="""Users should change their password 

    The users are still infected, therefore, changing the password won’t help much, particularly if the malware has a keylogger. 

    We need to stop the malware propagation! 
    """
    print("a6",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(8)
    return

def a7():
    nar="""Propagate malicious file hash
    
    Antiviruses remove the malware from the infected users’ machine in some cases. However, if the malware is polymorphic, this approach won't be effective!

    We need to stop the malware propagation!"""
    print("a7",nar)
    #some machines turns green
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(8)
    cur.execute("update Items set Skin_color = 0 where ID=16")
    cur.execute("update Items set Skin_color = 0 where ID=20")
    time.sleep(8)
    return

def a8():
    nar=""" Disconnect internet
    
    While this would stop major damage from the attack, this would cause far too much disruption to be a sensible option. User satisfaction drops right down.

    What should we do next?
    """
    print("a8",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    satisfaction(-33)
    time.sleep(8)
    return

def q3():
    q="How can we stop the malware propagation?"
    print("Q3", q)
    a=['Manually remove the malware from the remaining machines', 'Create a separate VLAN isolated from all other VLANs and place all infected machines on that VLAN.', 'Close the port (port 80) that the malware is using to spread.']
    cur.execute("update Narration set Content = ''")
    cur.execute("delete from Questions")
    cur.execute("insert into Questions (ID, Content) values (3, ?)", (q,))
    for i in a:
        cur.execute("insert into Answers (ID, Content, Question_ID) values (?,?,3)", (a.index(i) +1,i))
    return

def a9():
    nar="""Manually remove malware
    
    This is very challenging and would take too long to implement. This would give the malware time to spread, infect, and compromise more devices.
    """
    print("a9",nar)
    #show spreading faster than it can be contained ? 1 machine turns green 5 amber ?
    #right now limited pool of devices
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(2)
    cur.execute("update Items set Skin_color = 0 where ID = 30")
    cur.execute("update Connections set Active = 1, Direction = 1 where Item_ID = 28 and Item_ID_2 IN (29,31,32)")
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (28,  29, 1, 1) ")
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (28,  31, 1, 1) ")
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (28,  32, 1, 1) ")
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID IN (29,31,32)")
    cur.execute("select Item_ID from Runtime inner join Items on Items.ID = Runtime.Item_ID where Room_ID not in (2,3) and Items.Item_type_ID in (4,13,15,19,35) and Skin_color = 0 and Building_ID = 1 order by random() limit 5")
    infect=list(map(lambda x: x[0],cur.fetchall()))
    cur.execute("select ID from Items inner join Runtime on Runtime.Item_ID = Items.ID where Skin_color = 1 and Building_ID = 1 order by random() limit 1")
    l=cur.fetchone()[0] # take a random infected machine to initiate infections
    for i in infect:
        cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?, ?, 1, 1)", (l, i)) #display connection attempts
        time.sleep(2)
        cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID =? ", (i,))
    time.sleep(8)
    return

def a11():
    nar="""Close port 80 
    
    This is one of the core ports used by Internet! Closing this port is too disruptive and will cause the user satisfaction to drop very low, since no one will be able work. 

    """
    print("a11",nar)
    satisfaction(-33)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(8)
    return

def a10():
    nar="""Isolate infected machines on a separate VLAN 
    
    This will significantly help slow down the spread!
    """
    print("a10",nar)
    # remove connection between infected and non infected/ Connections are not everlasting though
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(5)
    cur.execute("update Connections set Active = 0")
    time.sleep(8)
    return

def q4():
    q="What can we do to prevent being infected by ransomware again in the future?"
    print("Q4", q)
    a=['Only allow users to download programs that have been approved by the security team', 'Add a rule to the firewall to prevent the malware from being downloaded again', 'Educate users on ransomware and safe browsing.', 'Insert ‘Canary files’ in the shared drives that if touched immediately flag an alert']
    cur.execute("update Narration set Content = ''")
    cur.execute("delete from Questions")
    cur.execute("insert into Questions (ID, Content) values (4, ?)", (q,))
    for i in a:
        cur.execute("insert into Answers (ID, Content, Question_ID) values (?,?,3)", (a.index(i) +1,i))
    return


def a12():
    nar="""Whitelist Applications 
    
    This would absolutely swamp the security team with constant requests to have applications approved. 
    
    User satisfaction drops to 0. 
    """
    print("a12",nar)
    #satisfaction = 0, manual request 
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(6)
    cur.execute("update User_satisfaction set Value = 0")
    time.sleep(8)
    return

def a13():
    nar="""Add rules to the firewall 
    
    While this approach might stop this specific ransomware, it will not be effective with other ransomware. 
    """
    print("a13",nar)
    #jump in time ?
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(8)
    return

def a14():
    nar="""Educate employees and student
    
    This might help, but people do still make mistakes and malware authors are very creative and will find ways to deceive users.
    
    """
    print("a14",nar)
    #how to show education and future impact ?
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(8)
    return

def a15():
    nar="""Use canary files 
    
    We have now placed a few canary files. Let's see what happens when a ransomware attempts to encrypt these files. """
    print("a15",nar)
    #jump in time, 1 machine gets amber, show canary files and isolation ?
    #explain the jump in time ? reset db show one pc connecting to file server and then going green ?
    cur.execute("update Narration set Content = ?", (nar,))
    cur.execute("update Connections set Active = 0")
    cur.execute("update Items set Skin_color = 0")
    time.sleep(7)
    nar = """ Attempt to encrypt canary file! """   
    nar2 = """A ransomware on an infected computer tried to encrypt a canary file """
    cur.execute("update Narration set Alert = ? , Content = ?", (nar, nar2))
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID = 17")
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (17,  3, 1, 1) ")
    time.sleep(7)
    nar = """ The computer is automatically isolated from the network, preventing further damage, and the program touching that file is killed"""
    cur.execute("update Narration set Alert = '' , Content = ?", (nar,))
    cur.execute("update Items set Skin_color = 0 , State = 'Secure', Text_placeholder_1 = '' , Text_placeholder_2 = '' , Text_placeholder_3 = ''")
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (17,  3, 0, 1) ")
    cur.execute("update Connections set Active = 0 where Item_ID = 17")
    time.sleep(8)                                                                       
    return


def finish():
    global end_time
    end_time = time.time()
    elapsed_time = end_time - start_time
    time_spent = convert(elapsed_time)
    cur.execute("select Value from User_satisfaction")
    r=cur.fetchone()
    # cur.execute("update Narration set Alert = ?",  Content = ''")
    nar = """Scenario Ended

    The scenario has ended! Based on your actions, University's users are """+ str(r[0]) + """% satisfied about their network access.
    You spent """+ time_spent +""" to finish the scenario."""
    cur.execute("update Narration set Content = ? , Alert = ''", (nar,))
    cur.execute("Update Timer set Value = ?", (int(elapsed_time),))
    time.sleep(8)
    return

def restart():
    q = """Would you like to restart the scenario ?"""
    a= ['RESTART', 'BACK TO MAIN MENU']
    cur.execute("update Narration set Content = ''")
    cur.execute("delete from Questions")
    cur.execute("insert into Questions (ID, Content) values (1, ?)", (q,))
    cur.execute("delete from Answers")
    for i in a:
        cur.execute("insert into Answers (ID, Content, Question_ID) values (?,?,1)", (a.index(i) +1,i))
    return

def reset():
    c="""delete from Connections ; Update Answers set Content = '' ; update Items set Skin_color = 0 , Text_placeholder_1 = '' ,
    Text_placeholder_2 = '' , Text_placeholder_3 = '', State = 'Secure' ; delete from Narration ;
    Insert into Narration Values('','',0,'',NULL) ; delete from Questions ; Insert into Questions VALUES(1,'') ;
    Update User_satisfaction set Value = 100 ; Update Timer set Value = 0 """
    cur.executescript(c)
    return

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 

def satisfaction(n):
    cur.execute("select Value from User_satisfaction") # get current value of satisfaction to 
    r=cur.fetchone()[0]
    o = r + n
    cur.execute("update User_satisfaction set Value = ?", (o,))
    return(0)


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


def main():
    reset()
    global c
    global start_time
    c=0
    start()
    answer_monitor()
    c=0
    start_time = time.time()
    bit1()
    bit2()
    bit3()
    bit4()
    q1()
    answer_monitor()
    if c == 1:
        a1()
    elif c == 2:
        a2()
    elif c == 3:
        a3()
    elif c == 4:
        a4()
        print("finished")
        return
    c=0
    q2()
    answer_monitor()
    if c == 1:
        a5()
    elif c == 2:
        a6()
    elif c == 3:
        a7()
    elif c == 4:
        a8()
    c=0
    q3()
    answer_monitor()
    if c == 1:
        a9()
    elif c == 2:
        a10()
    elif c == 3:
        a11()
    c=0
    q4()
    answer_monitor()
    if c == 1:
        a12()
    elif c == 2:
        a13()
    elif c == 3:
        a14()
    elif c == 4:
        a15()
    c=0
    finish()
    print("finished")
    restart()
    answer_monitor()
    if c == 1:
        reset()
        main()

    if c == 2:
        reset()
        os.system('python master.py')
    return

main()

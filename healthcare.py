# Healthcare - Last Modified by Irene Thursday 
# Healthcare - Last Modified by Irene
import os, sqlite3, time, random
con=sqlite3.connect("database.db", isolation_level=None)
cur=con.cursor()

p0 = 358
hospital_server = 380
uni_vpn = 177
uni_cred = 180
attacker = 540 # from smart home
#usable devices' type id ? 19,55,56,16,13,35 (server:id=380)

start_time = 0
end_time = 0

def start():
    q = """ <size=65><b>Welcome</b></size=65>

    This is a demonstration of a cyber attack in a healthcare enviroment that can also pivot to a University facility. 
    
    As the attack progresses you can observe how various machines will be affected.  
    
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
    nar = """ <size=50><b> Beginning of the Attack </b></size=50>

    A phishing email is sent to the receptionist of the Hospital asking them to log in to the HR system and confirm urgently the number of 
    annlual leave days they have left. 
    
    Zoom in to the Hospital building to HR office to observe how the cyber attack will play out.
    """
    print(1,nar)
    cur.execute("update Narration set Content = ?", (nar,)) # if sure no duplicates just update
    time.sleep(8)
    return

def bit2():
    time.sleep(2)
    nar = """ <size=50><b> Phising Successful </b></size=50>

    Employee clicks on the link in the fake email and is redirected to a fake web page. It looks identical to the hospital's HR management system.

    They log in to the web page with their credentials.
    """
    cur.execute("update Narration set Alert = ? , Content = ''", (nar,))
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Phishing attack' , Text_placeholder_2 = '' , Text_placeholder_3 = 'Confidence: 99%' , State = 'Compromised' where ID=?", (p0,))
    cur.execute("update Items set Skin_color = 1, State = 'Compromised' where ID = 361")
    nar2="""Zoom in to the compromised computer to see the fake web portal"""
    time.sleep(5)
    cur.execute("update Narration set Content = ?", (nar2,))
    time.sleep(8)
    return

def bit3():
    time.sleep(2)
    nar="""  <size=50><b> Credentials are stolen </b></size=50>

    The user is now redirected to the real HR system log in page and to them, it seems like they have entered their password incorrectly.
    """
    print(3, nar)
    cur.execute("update Narration set Alert = ? , Content = ''", (nar,))
    time.sleep(7)
    return
#bit4 not yet ? bit9
def bit4():
    time.sleep(2)
    nar= """ <size=50><b> Warning </b></size=50>

    Attacker connects to hospital's VPN!
    
    Having stolen the employees credentials, the attacker has now successfully logged in to the hospitals VPN network!  
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  ?, 1, 0) ", (attacker, hospital_server))
    time.sleep(7)
    return

def bit5():
    time.sleep(2)
    nar= """ <size=50><b> Malware Launched </b></size=50>
    
    Having gained access to the network, the attacker is now launching a worm (i.e. worm.win32.kino.kf). 
    
    The worm is able to find vulnerable nearby machines and can compromise them by bruteforcing their credentials. 
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))

    nar2="""Zoom out to hospital view to see which machines will be affected by the malware!"""
    cur.execute("update Narration set Content = ?", (nar2,))
    cur.execute("select Item_ID from Runtime inner join Items on Items.ID = Runtime.Item_ID where Building_ID = 8 and Item_type_ID = 19 order by random() limit 3")    
    infect = list(map(lambda x: x[0],cur.fetchall()))
    cur.execute("select ID from Items where ID = 380")
    infect.append(cur.fetchone()[0])
    for i in infect:
        cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  ?, 1, 0) ", (p0,i))
        time.sleep(1)
        cur.execute("update Items set Skin_color = 1 where ID = ?", (i,))
        time.sleep(1)   
    time.sleep(8)
    return    

def bit6():
    time.sleep(2)
    nar= """  <size=50><b> PACS server compromised </b></size=50>
    
    A backdoor on the server allows the attacker to extract sensitive patient data and usernames/passwords of hospital emploees who have previously logged onto the server. 
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    cur.execute("update Items set Skin_color= 2 , State = 'Compromised', State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID = ?", (hospital_server,))                                                                                                                                                                                                                                                                                                                      
    time.sleep(3)
    nar3= """ <size=50><b> Warning </b></size=50>
    Sensitive information is now leaked and sent to unknown IP addresses.
    """
    cur.execute("update Narration set Alert = ?", (nar3,))
    nar2="""Zoom into the MRI room where the Picture Archiving and Communication System (PACS) is located. This is a medical imaging technology which holds sensitive medical patient data!
    
    The attacker has identified that one of the PACS servers is using an outdated OS and have managed to bruteforce its credentials!
    """
    cur.execute("update Narration set Content = ?", (nar2,))
    time.sleep(8)
    return

def bit7():
    time.sleep(2)
    nar= """ <size=50><b> Warning </b></size=50>

    Some suspicious activity on the network has been detected. 

    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    time.sleep(6)
    return          

def q1():
    q= " What can we do at this stage?"
    print("Q1", q)
    a= ['Cross reference access logs with scan event and reset paswords for all the accounts', 'Run an AntiVirus (AV) software on compromised computers', 'Shut down the server' ]
    cur.execute("update Narration set Content = ''")
    cur.execute("delete from Questions")
    cur.execute("insert into Questions (ID, Content) values (1, ?)", (q,))
    cur.execute("delete from Answers")
    for i in a:
        cur.execute("insert into Answers (ID, Content, Question_ID) values (?,?,1)", (a.index(i) +1,i))
    return

def a1():
    nar = """ <size=50><b><size=50>Cross reference logs</b></size=50>
    
    This will allow us to block the compromised accounts from which the attacker has retrieved their credentials, however, given the backdoor that is on the server the adversary could 
    restart the process are retrieve more account details.
    
    What should we do next?
    """
    print("a1",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(11)
    return


def a2():
    nar=""" <size=50><b>Run AV software</b></size=50>
    
    Unfortunately the virus is so old that the Anti virus software did not recognize it. 
    
    """
    print("a2",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(5)
    return


def a3():
    nar = """ <size=50><b>Shut down PACS server</b></size=50>

    This is an extreme measure, which might lead to financial loss and disrupt the patient treatment. 

    User satisfction drops. 
    """
    print("a3",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    satisfaction(-50)
    time.sleep(5)
    return

def bit8():
    time.sleep(2)
    nar= """ <size=50><b>Measure ineffective</b></size=50>
    
    In the meantime, the attacker scans the internal hospital network and identifies an open VPN server connecting another network. 
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ? , Content = ''", (nar,))
    time.sleep(6)
    return

def bit9():
    time.sleep(2)
    nar= """ <size=50><b>University VPN credentials Stolen </b></size=50>
    
    The attacker successfuly steals VPN credentials from PACS server and logs onto the VPN. 
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    time.sleep(7)
    return


def bit10():
    time.sleep(2)
    nar= """ <size=50><b>Attacker performs Recon</b></size=50>
    
    Having accessed the network, the attakcer scans the network and identifies an IP range. Following an IP lookup, they identify that the server is part of a University medical research lab.
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  ?, 1, 0) ", (hospital_server, uni_vpn))
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' where ID = ?", (uni_vpn,))
    nar2 = """Zoom out to the map level to observe how the adversary will pivot to the University's network! 
    """
    cur.execute("update Narration set Content = ?", (nar2,))
    time.sleep(7)
    return

def bit11():
    time.sleep(2)
    nar= """ <size=50><b> Warning </b></size=50>
    Attacker has now access to the University's network
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    time.sleep(5)
    return

def bit12():
    time.sleep(2)
    nar= """ <size=50><b>Attacker identifies credential server</b></size=50>
    
    The adversary is now able to extract hashed credentials for local IT systems on which experimental virus vaccination experiment details are stored. 
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  ?, 1, 0) ", (uni_vpn,uni_cred))
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised' where ID = ?", (uni_cred,))
    nar2 = """Zoom in to the University's medical research lab! 
    """
    cur.execute("update Narration set Content = ?", (nar2,))
    time.sleep(7)
    return

def bit13():
    time.sleep(2)
    nar= """ <size=50><b>Warning </b></size=50>
    
    Suspisious scanning actvity is detected on the network!
    
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))

    nar2 = """We need to take action!
    """
    cur.execute("update Narration set Content = ?", (nar2,))
    time.sleep(7)
    return




def q2():
    q= "What shoud we do?"
    print("Q2", q)
    a=['Restore the server to previous state', 'Reset every account logged onto the server', 'Lock the account that triggered the event']
#    cur.execute("update Items set Icon='folder.xyz' where Skin_color = 1 or Skin_color = 'red.xyz'")
    cur.execute("update Narration set Content = ''")
    cur.execute("delete from Questions")
    cur.execute("insert into Questions (ID, Content) values (2, ?)", (q,))
    for i in a:
        cur.execute("insert into Answers (ID, Content, Question_ID) values (?,?,2)", (a.index(i) +1,i))
    return

def a4():
    nar=""" <size=50><b>Restore server</b></size=50>

    This takes time and it is quite disruptive. The compromised credentials are still effective.
    """
    print("a5",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(4)
    return
    

def a5():
    nar="""<size=50><b>Reset Accounts</b></size=50>

    This will disrupt the service, but may be partially effective in mitigating credential theft. 
    """
    print("a6",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(7)
    return

def a6():
    nar="""<size=50><b>Lock account</b></size=50>
    
    This might lock the current account that the adversary is using, but they have compromised a number of different accounts! It won't be very effective.
    """
    print("a7",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(8)
    return

def bit14():
    time.sleep(2)
    nar= """ <size=50><b>Measure ineffective</b></size=50>
    
    In the meantime, the attacker accesses the sensitive data on local IT and exfiltrates it to their own servers.   
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  460, 1, 0) ", (uni_vpn,))
    time.sleep(6)
    return

def bit15():
    time.sleep(2)
    nar= """ <size=50><b> Alert </b></size=50>
    Network traffic is bursting!
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    cur.execute("update Network_activity set Value = 90")
    time.sleep(5)
    return



def q3():
    q="What can we do at this stage?"
    print("Q3", q)
    a=['Block IP address', 'Restore the server', 'Kill the VPN session and reset account credentials', 'Lock accounts aythenticated on the server']
    cur.execute("update Narration set Content = ''")
    cur.execute("delete from Questions")
    cur.execute("insert into Questions (ID, Content) values (3, ?)", (q,))
    for i in a:
        cur.execute("insert into Answers (ID, Content, Question_ID) values (?,?,3)", (a.index(i) +1,i))
    return

def a7():
    nar="""<size=50><b> Block IP </b></size=50>
    
    This won't be very effective as the attackers can change their IP address. 
    """
    print("a9",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(6)
    return

def a8():
    nar="""<size=50><b>Restore Server</b></size=50>
    
    This might stop the data leakage temporarily, but the attackes can attempt to exctract the data again at the later time. 

    """
    print("a11",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(8)
    return

def a9():
    nar="""<size=50><b>Kill VPN session</b></size=50>
    
    This might stop the data leakage temporarily, but the attackes can attempt to exctract the data again at the later time. 

    """
    print("a11",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(8)
    return

def a10():
    nar=""" <size=50><b>Lock accounts</b></size=50>
    
    This is an extreme measure which will also prevent legitimate researchers from working. However, it will freeze the attack. 
    """
    print("a10",nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(5)
    satisfaction(-20)
    return

def bit16():
    time.sleep(2)
    nar= """ <size=50><b>Ransomware Activated</b></size=50> 

    In the meantime, to cover their tracks the attacker launches a ransomware attack on the entire hospital IT infrastructure. 
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    nar2="""<size=50><b> Alert </b></size=50>
    
    Log files are encrypted! 
    """
    cur.execute("update Narration set Alert = ?", (nar2,))
    cur.execute("select ID from Items where Skin_color = 1 order by random() limit 1")
    r=cur.fetchone()[0]
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  349, 1, 0) ", (r,))
    cur.execute("update Items set Skin_color = 2, State = 'Compromised' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' , State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Not Petya' , Text_placeholder_3 = 'Confidence: 95%' where ID in (349, 358, 378, 380, 527)")
    cur.execute("update Items set Skin_color = 2 , State = 'Compromised', State = 'Compromised', Text_placeholder_1 = 'Ransomware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID = ?", (uni_cred,)) 
    time.sleep(7)
    return

def bit17():
    time.sleep(2)
    nar= """ <size=50><b> Alert </b></size=50>

    Ransomware Detected 
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    time.sleep(7)
    return



def q4():
    q="Whilst the sample of the detected malware is being analysed, what should we do?"
    print("Q4", q)
    a=['Disconnect the Internet', 'Isolate the infected devices', 'Restore critical parts of the compromised infrastracture and shut down the rest', 'Block the protocol used by ransomware']
    cur.execute("update Narration set Content = ''")
    cur.execute("delete from Questions")
    cur.execute("insert into Questions (ID, Content) values (4, ?)", (q,))
    for i in a:
        cur.execute("insert into Answers (ID, Content, Question_ID) values (?,?,3)", (a.index(i) +1,i))
    return


def a11():
    nar="""<size=50><b>Disconnect Internet </b></size=50>
    
    Extreme measure, patients' health is at risk. The ransomware keeps running on the infected hosts.  
    
    User satisfaction drops. 
    """
    print("a12",nar)
    #satisfaction = 0, manual request 
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(6)
    cur.execute("update User_satisfaction set Value = 0")
    return

def a12():
    nar="""<size=50><b>Isolate infected devices</b></size=50>

    This will prevent further contamination, but we can't be sure that we have eradicated the ransomware. 
    """
    print("a13",nar)
    #jump in time ?
    cur.execute("update Narration set Content = ?", (nar,))
    cur.execute("update Connections set Active = 0")
    time.sleep(5)
    return

def a13():
    nar="""<size=50><b>Restore critical IT parts </b></size=50>
    
    Offline backups should help restore the compromised network components to the previous healthy state. However, we can be sure that the malware has been eradicated.
    
    """
    print("a14",nar)
    #how to show education and future impact ?
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(5)
    return

def a14():
    nar="""<size=50><b>Block ransomware's protocol</b></size=65>

    This will help to prevent further replication, however, the already infected hosts will still have their files encrypted. 
    
    """
    print("a15",nar)
    #jump in time, 1 machine gets amber, show canary files and isolation ?
    #explain the jump in time ? reset db show one pc connecting to file server and then going green ?
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(5)
    return


def finish():
    global end_time
    end_time = time.time()
    elapsed_time = end_time - start_time
    time_spent = convert(elapsed_time)
    cur.execute("select Value from User_satisfaction")
    r=cur.fetchone()
    nar = """ <size=80>Congratulations!</size=80>
    
    The scenario has ended. Based on your actions Hospital's users are """+ str(r[0]) + """% satisfied about their network access.
    You spent """+ time_spent +""" to finish the scenario"""
    cur.execute("update Narration set Content = ? , Alert = ''", (nar,))
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
    c=0
    start()
    answer_monitor()
    c=0
    start_time = time.time()
    bit1()
    bit2()
    bit3()
    bit4()
    bit5()
    bit6()
    bit7()
    q1()
    answer_monitor()
    if c == 1:
        a1()
    elif c == 2:
        a2()
    elif c == 3:
        a3()
        print("finished")
        restart()
        answer_monitor()
        if c == 1:
            reset()
            main()
        return
    c=0
    bit8()
    bit9()
    bit10()
    bit11()
    bit12()
    bit13()
    q2()
    answer_monitor()
    if c == 1:
        a4()
    elif c == 2:
        a5()
    elif c == 3:
        a6()
    c=0
    bit14()
    bit15()
    q3()
    answer_monitor()
    if c == 1:
        a7()
    elif c == 2:
        a8()
    elif c == 3:
        a9()
    elif c == 4:
        a10()
    c=0
    bit16()
    bit17()
    q4()
    answer_monitor()
    if c == 1:
        a11()
    elif c == 2:
        a12()
    elif c == 3:
        a13()
    elif c == 4:
        a14()
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

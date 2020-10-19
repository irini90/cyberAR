#Manufacturing plant Irene/Thursday
import os, sqlite3, time, random
con=sqlite3.connect("database.db", isolation_level=None)
cur=con.cursor()

p0 = 585
historian = 605
scada = 580
home = 540
#factory = 31 / office = 39 
#router office 591
#router lab? 596


def start():
    q = """ <size=65> Welcome </size=65>
    
    This is a demonstration of a cyber attack within small/medium sized a pharmaceutical company which is developing a new drug for Coronavirus. 
    
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
    nar = """ <size=50>Beginning of the Attack </size=50>

    A phishing email is sent to the newest/inexperienced employee of the company. The fake email seems to be from the chief engineer.

    """
    print(1,nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(9)
    nar2=""" <size=50>The Fake Email </size=50>
    
    The chief engineer is instructing the employee to update all the PLC, HMI, SCADA/Historian firmware in the field network.
    
    The email contains a link from which the employee should download the software. """
    cur.execute("update Narration set Content = ?", (nar2,))
    time.sleep(6)
    
    return

def bit2():
    time.sleep(2)
    nar = """ <size=50>Phishing Successful</size=50>
    
    Employee clicks on fake email!
    
    They are then redirected to a fake vendor web page containing various malicious verisions of the firmware/software for the plant systems.
    """
    cur.execute("update Narration set Alert = ?", (nar,))
    cur.execute("update Items set Skin_color = 1 , State = 'Compromised', Text_placeholder_1 = 'Phishing attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 90%' where ID=?", (p0,))
    nar2="""The page looks identical to the legitimate vendor's page, so they download the malicious software. Zoom in to the compromised computer to see the fake web page"""
    cur.execute("update Narration set Content = ?", (nar2,)) 
    time.sleep(6)
    return

def bit3():
    time.sleep(2)
    nar=""" <size=65>Alert</size=65>
    
    Employee downloads malicious software from the fake website!  
    """
    print(3, nar)
    cur.execute("update Narration set Alert = ?", (nar,)) 
    time.sleep(6)
    return


def bit4():
    time.sleep(2)
    nar=""" <size=65>Alert </size=65>
    
    The employee transfers malicious software from his corporate PC to the plant engineering workstation via USB drive. 
    """
    print(3, nar)
    cur.execute("update Narration set Alert = ? , Content = ''", (nar,))
    time.sleep(2)
    nar2 = """ They notice that the extraction process of the new software is a bit different than what they experiencd in the training course, but they don't think anything of it."""
    cur.execute("update Narration set Content = ?", (nar2,)) 
    time.sleep(2)
    nar3 = """They proceed to upgrade the firmware on the plant's PLCs/HMIs/Historian/SCADA PC."""
    cur.execute("update Narration set Content = ?", (nar3,)) 
    # cur.execute("select ID from Items where Item_type_ID in (20, 21, 22, 23, 24, 6)") #with dispenser pump
    # infect = list(map(lambda x: x[0],cur.fetchall()))
    infect = [historian, scada, 437, 439, 433, 436, 437, 439]
    for i in infect:
        cur.execute("update Items set Skin_color = 1, State = 'Compromised', Text_placeholder_1 = 'Malicious firmware' , Text_placeholder_2 = '' , Text_placeholder_3 = 'Confidence: 90%' where ID = ?", (i,))
        time.sleep(1.7)  
    time.sleep(1.7)
    cur.execute("update Items set Skin_color = 1, State = 'Compromised', Text_placeholder_1 = 'Malicious software' , Text_placeholder_2 = '' , Text_placeholder_3 = 'Confidence: 90%' where ID = ?", (scada,))
    time.sleep(5)
    return

def bit5():
    time.sleep(2)
    nar= """ <size=50> Warning </size=50>
        
    The SCADA and Historian PC’s are compromised. A series of DLL files which were altered during the upgrade contain malicious code that is acting in part as a command and control server for the PLC data extraction.  
    """ 
    cur.execute("update Items set Skin_color = 2, State = 'Compromised' where ID = 436")
    cur.execute("update Items set Skin_color = 2, State = 'Compromised' where ID = 439")
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    time.sleep(8)
    return

def bit6():
    time.sleep(2)
    nar= """ <size=50> Data Leakage </size=50>
    
    A malware has also been installed with the firmware/software update. This is occasionally transferring data - containing PLC readings and process details- to specific IP addresses from the compromised Historian PC.
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    nar2="""Such information is valuable to attackers as they can steal important information e.g. ingredient ratios for pills, which a) they can sell to competitors and b) create adversarial data."""
    cur.execute("update Narration set Content = ?", (nar2,))
    cur.execute("insert into Connections (Item_ID, Item_ID_2, Active, Direction) values (?,  ?, 1, 0) ", (historian,home))
    time.sleep(6)
    return

def bit7():
    time.sleep(2)
    nar= """ <size=50> 1 month later </size=50>
    
    For a while the adversaries have been silently exfiltrating data, but have not performed any active attacks. 

    Until now.."""
    cur.execute("update Narration set Content = ? , Alert = ''", (nar,))
    time.sleep(4)
    return    

def bit8():
    time.sleep(2)
    nar= """ <size=50> Operation Distruption </size=50>

    The Automation team starts receiving work orders detailing strange behaviour in plant processes as some of the tablets are failing the quality control, and some others are not but they are not sure what has happened. 
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ? , Content = ''", (nar,))
    time.sleep(7)
    return

def bit9():
    time.sleep(2)
    nar= """ <size=50>Drug Contamination </size=50>
    
    Due to the malicious firmware, the dispensing pumps are  altering the ratio of the ingredients at random times leading to contaminated pills (not all pills will be contaminated, just a few every now and then).
    """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    time.sleep(7)
    return


def bit10():
    time.sleep(2)
    nar= """ <size=50> The process </size=50>
    Normal Functioning UR3 Robotic arms are in operation. Once the two types of pills are produced, they are dropped onto the production line. From there, they will be picked up by a robotic arm and they will be sorted to be packaged. The arm will separate these in two different containers.
    """
    print(4,nar)
    cur.execute("update Narration set Content = ?", (nar,))
    time.sleep(7)
    return

def bit11():
    time.sleep(2)
    nar= """ <size=65> Alert </size=65>
    
    UR3 Robots Compromised """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    cur.execute("update Items set Skin_color = 2 , State = 'Compromised', State = 'Compromised', Text_placeholder_1 = 'Malware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID = ?", (445,)) 
    cur.execute("update Items set Skin_color = 2 , State = 'Compromised', State = 'Compromised', Text_placeholder_1 = 'Malware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID = ?", (446,))
    cur.execute("update Items set Skin_color = 2 , State = 'Compromised', State = 'Compromised', Text_placeholder_1 = 'Malware attack' , Text_placeholder_2 = 'Version:Wannacry' , Text_placeholder_3 = 'Confidence: 95%' where ID = ?", (448,))  
    nar2=""" The attack targets the python code that instructs the arm to place the blue and violet pills in the blue and violet boxes respectively.
    
    The code completely replaces the original code of the robot, instructing it to place the blue pills in the violet containers and vice versa."""
    cur.execute("update Narration set Content = ?", (nar2,))
    time.sleep(7)
    return    

def bit12():
    time.sleep(2)
    nar= """ <size=50> Warning </size=50>
    
    ALtered pills are being modified. """
    print(4,nar)
    cur.execute("update Narration set Alert = ?", (nar,))
    nar2=""" The mixed up/contaminated pills will reach the packaging process. There they will be put into foiled consumer packaging and will be ready for distribution."""
    cur.execute("update Narration set Content = ?", (nar2,))
    time.sleep(7)
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


def finish():
    cur.execute("select Value from User_satisfaction")
    r=cur.fetchone()
    nar = """ <size=65>The scenario has ended<size=65>"""
    cur.execute("update Narration set Content = ? , Alert = ''", (nar,))
    time.sleep(8)
    return


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
    bit1()
    bit2()
    bit3()
    bit4()
    bit5()
    bit6()
    bit7()
    bit8()
    bit9()
    bit10()
    bit11()
    bit12()
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

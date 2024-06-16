import sqlite3
from tkinter.messagebox import showwarning
import random 
import string
from mymodules.genempno import Employee,gen_id

import qrcode
from PIL import Image,ImageTk
from tkinter import Canvas
from mymodules.setsec import setsec
import pyotp
from tkinter.simpledialog import askstring
# conn = sqlite3.connect('college.db')
# cursor = conn.cursor()

def connect():
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS  login1(emp_id VARCHAR(50) PRIMARY KEY,fname VARCHAR(50),lname VARCHAR(50),password VARCHAR(100),sec VARCHAR(100),date DATE,key VARCHAR(50) UNIQUE);')
    conn.commit()
    # cursor = conn.cursor()
    return conn
def login_back(username,sec,passwd,):
        conn = connect()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT password FROM login1 WHERE emp_id= ? AND sec= ?", (username, sec))
            a = cursor.fetchone()
            if a and a[0] == passwd:
            # print("Password verified")
            # q2 = "Select key from login1 WHERE emp_id=?"
                n = cursor.execute("Select key from login1 WHERE emp_id = ?", (username,))
                n = n.fetchone()
                n = n[0]
                return n
            elif username == '' and passwd == '':
                showwarning(title="Validation", message="Please Enter your credentials")
            else:
                showwarning(title="Validation", message="Login Failed")
        except Exception as e:
                showwarning(title="Validation", message=f"Failed to connect to Database: {str(e)}")



def verify_code1(user_ent,cbs,otp_ent):
        conn = connect()
        cursor = conn.cursor()
        try:
            username  = user_ent.get()
            sec = cbs.get()
            cursor.execute("SELECT key FROM login1 WHERE emp_id= ? AND sec= ?", (username, sec))
            
            k = cursor.fetchone()
            otp = otp_ent.get()
            print(k[0])
            print(username,sec,k[0],otp)
            totp = pyotp.TOTP(k[0])
                # input_code = int(otp)
            print(totp.now())
            print()
            if totp.verify(otp) == True:
                    m = askstring(title="Reset Pass",prompt="Enter New Password")
                    print(m)
                    try:
                        # cursor = conn.cursor()
                        cursor.execute('UPDATE login1 set password = ? where emp_id ==  ?',(m,username,))
                        conn.commit()
                    except Exception as e :
                        print(e)
            else:
                showwarning(title="2fa",message="Invalid Otp")
        except Exception as e:
            print(f"An Error occurred {e}" )
def signup_backend(id='',firstname='',lastname='',password='',sect='',dob='',key=''):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO login1(emp_id,fname,lname,password,sec,date,key)VALUES (?, ?, ?, ?, ?, ?, ?) ',(id, firstname, lastname, password, sect, dob, key))
    conn.commit()
connect()
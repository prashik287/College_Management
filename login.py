import tkinter as tk
from tkinter import ttk
from tkinter import *
from pynput.keyboard import *
from tkinter.messagebox import showinfo, showwarning, askokcancel,showerror
import sqlite3
import pyotp
import qrcode
import random
import string
from mymodules.setsec import setsec
from login_backend import login_back,verify_code1,signup_backend
from PIL import Image, ImageTk
from mymodules.keygen import keygen
from mymodules.genempno import Employee, gen_id
from tkcalendar import DateEntry
from datetime import date
from password_validation import PasswordPolicy

import subprocess
from tkinter.simpledialog import askinteger,askstring

conn = sqlite3.connect('college.db')
cursor = conn.cursor()
def __Fee__():
    filename = 'Fee_Frontend.py'
    subprocess.run('python ' + filename)


def __Library__():
    filename = 'Library_Frontend.py'
    subprocess.run('python ' + filename)


def __Admission__():
    filename = 'Std_info_FrontEnd.py'
    subprocess.run('python '+ filename)

def __Admin__():
    filename = 'admin_Frontend.py'
    subprocess.run('python '+ filename)


def __Exam__():
       filename = "Search_Page.py"
       subprocess.run('python ' + filename)
def __FACULTY__():
        filename = "Facinfo_Frontend.py"
        subprocess.run('python '+ filename)

def verify_code(key,sec):
    totp = pyotp.TOTP(key)
    input_code = askinteger(title="OTP",prompt="Use Authenticator")
    if totp.verify(input_code) == True:
        if sec == "Admission":
            __Admission__()
        elif sec == "Fee":
            __Fee__()
        elif sec == "Exam":
            __Exam__()
        elif sec == "Library":
            __Library__()
        elif sec == "Faculty":
            __FACULTY__()
        elif sec == "Admin":
            __Admin__()
        else:
            showwarning(title="Warning",message="Unknown Section")       
    else:
        showwarning(title="Warning",message="Failed to verify")

def login(user_ent,pass_ent,cb):
    username = user_ent.get()
    passwd = pass_ent.get()
    sec = cb.get()
    # print(username, passwd, sec)
    # try:
    #     cursor.execute("SELECT password FROM login1 WHERE emp_id= ? AND sec= ?", (username, sec))
    #     a = cursor.fetchone()
    #     if a and a[0] == passwd:
    #         # print("Password verified")
    #         # q2 = "Select key from login1 WHERE emp_id=?"
    #         n = cursor.execute("Select key from login1 WHERE emp_id = ?", (username,))
    #         n = n.fetchone()
    #         n = n[0]
    #         # print(n)
    n = login_back(username,sec,passwd)
    verify_code(n, sec)

    #     elif username == '' and passwd == '':
    #         showwarning(title="Validation", message="Please Enter your credentials")
    #     else:
    #         showwarning(title="Validation", message="Login Failed")
    # except Exception as e:
    #         showwarning(title="Validation", message=f"Failed to connect to Database: {str(e)}")

# def setsec(cb1):
#         sec = cb1.get()
#         if sec == "Admission":
#             return "AD"
#         elif sec == "Fee":
#             return "FE"
#         elif sec == "Exam":
#             return "EX"
#         elif sec == "Library":
#             return "LIB"
#         elif sec == "Faculty":
#             return "FAC"
# def insdb(cb1,firstname,lastname,mypass,ldate,sec):

#     try:
#         a = ''.join(random.choices(string.ascii_lowercase, k=10))
#         # print(a)
#         emp = Employee(gen_id(setsec(cb1)), firstname=firstname, lastname=lastname, password=mypass, dob=ldate, sect=sec,
#                        key=a)
#         emp.show_info()
#         m2fa(a, emp.firstname, "College-Management")
#         query = '''INSERT INTO login1(emp_id,fname,lname,password,sec,date,key)
#                     VALUES (?, ?, ?, ?, ?, ?, ?) 
#                     '''
#         my_data = (emp.id, emp.firstname, emp.lastname, emp.password, emp.sect, emp.dob, emp.key)
#         cursor.execute(query, my_data)
#         conn.commit()  # Don't forget to commit the changes to the database
#     except Exception as e:
#          showwarning(title="Database Error", message=f"Error : {e}")

def forgotpass():

    fog = Toplevel()
    fog.geometry("800x580")
    fog.title('Reset Password')
    fog.config(bg="lightskyblue")
    fw = tk.Frame(fog,background="lightskyblue",pady=50,padx=150)
    titllab2 = Label(fw,background='lightskyblue',text="Reset Password",font=('arial',40),padx=5)
    titllab2.grid(row=3, column=5)
    cblab1 = Label(fw,text="Section : ",background="lightskyblue",font=('arial', 18))
    cblab1.grid(row=6,column=3)
    cbs = ttk.Combobox(fw)
    cbs['values'] = ("Admission",
                    "Fee",
                    "Exam",
                    "Library",
                    "Faculty")
    cbs.set("Select Section")

    cbs.grid(row=6, column=5,pady=30,padx=30)
    userlab = Label(fw, text="Employee id:", background="lightskyblue",font=('arial',18))
    userlab.grid(row=8,column=3)
    user_ent = Entry(fw)
    user_ent.grid(row=8, column=5)
    otp_lab = Label(fw, text="Enter OTP:", background="lightskyblue",font=('arial', 18))
    otp_lab.grid(row=10,column=3)
    otp_ent = Entry(fw)
    otp_ent.grid(row=10,column=5,pady=30,padx=30)


            # print("Password verified")
            # q2 = "Select key from login1 WHERE emp_id=?"
    # n = cursor.execute("Select key from login1 WHERE emp_id = ?", (username,))
    # n = n.fetchone()
    # n = n[0]
            # print(n)


    fog_btn = Button(fw,text="Reset Pass",width=10,command=lambda:verify_code1(user_ent,cbs,otp_ent))
    fog_btn.grid(row=11,column=5)
    fw.place(x=40,y=50)
    fog.mainloop()
try:


    root = Tk()
    root.geometry('650x450')
    root.title('Login')
    root.config(bg='Navajo white')

    nb = ttk.Notebook(root)
    nb.pack(expand=1, fill='both')

    frame1 = tk.Frame(nb, background='lightskyblue', pady=50, padx=150)

    titllab = Label(frame1, text="Login", font=('arial', 40), background="lightskyblue")
    titllab.grid(row=1, column=6)
    frame1.pack(fill='both', expand=2)

    # frame2 = tk.Frame(frame1, pady=14, background="lightskyblue")

    frame3 = tk.Frame(frame1, pady=14,padx=30, background="lightskyblue")
    cblab = Label(frame1,text="Section : ",background="lightskyblue",font=('arial', 16))
    cblab.grid(row=3,column=5,padx=30)
    cb = ttk.Combobox(frame1)
    cb['values'] = ("Admission",
                    "Fee",
                    "Exam",
                    "Library",
                    "Faculty",
                    "Admin")
    cb.set("Select Section")
    cb.grid(row=3, column=7,pady=30,padx=30)

    userlab = Label(frame1, text="Employee id:", background="lightskyblue",font=('arial', 16))
    userlab.grid(row=5,column=5)

    user_ent = Entry(frame1)
    user_ent.grid(row=5, column=7)

    frame4 = tk.Frame(frame1, pady=14, background="lightskyblue")
    passlab = Label(frame1, text="Password: ", background="lightskyblue",font=('arial', 16))
    passlab.grid(row=7, column=5)

    pass_ent = Entry(frame1, show="*")
    pass_ent.grid(row=7, column=7,pady=30,padx=30)

    btn = tk.Button(frame1, text="Login", pady=2, command=lambda : login(user_ent,pass_ent, cb))
    btn.grid(row=9, column=5, padx=30)
    # Bind the Enter key to the login function
    btnf = tk.Button(frame1,text="Forgot Password",pady=2,command=forgotpass)
    btnf.grid(row=9, column=7, padx=30)
    root.bind('<Return>', lambda event=None: btn.invoke())
    nb.add(frame1, text='Login')

    frame3.grid(row=1,column=1)
    frame4.grid(row=1,column=1)

    # ----------------------------------------------------------------login----------------------------------------------------------------#
    # ----------------------------------------------------------------Signup----------------------------------------------------------------#

    # signup label
    f5 = tk.Frame(nb, background='lightskyblue', pady=50, padx=28, height="2000")
    titllab = Label(f5, text="Sign up", font=('arial', 40), background="lightskyblue")
    titllab.pack()

    f6 = Frame(f5, background='lightskyblue', pady=50, padx=28)
    f6.columnconfigure(0, weight=1)
    f6.columnconfigure(1, weight=3)
    seclab = Label(f6, text="Section :", bg="lightskyblue", font=('arial', 18)).grid(row=0, column=0, sticky=tk.W)
    cb1 = ttk.Combobox(f6)
    cb1['values'] = ("Admission",
                    "Fee",
                    "Exam",
                    "Library",
                    "Faculty")
    cb1.set("Select Section")
    cb1.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
    fn = Label(f6, text="First Name :", font=('arial', 18), background="lightskyblue").grid(column=0, row=1, sticky=tk.W)
    fname = Entry(f6)
    fname.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
    ln = Label(f6, text="Last Name :", font=('arial', 18), background="lightskyblue").grid(column=0, row=2, sticky=tk.W)
    lname = Entry(f6)
    lname.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
    dob = Label(f6, text="Date of Birth : ", font=('arial', 18), background="lightskyblue").grid(column=0, row=3,
                                                                                                 sticky=tk.W)
    dt1 = date(2008, 12, 31)
    dt1.strftime(" %d. %B %Y %I:%M%p")
    cal = DateEntry(f6, selectmode='day', year=2020, month=5, day=22,
                               font=('arial', 17, 'bold'))
    cal.grid(row=3, column=1, padx=10, pady=5,sticky=tk.E)
    passl = Label(f6, text="Password :", font=('arial', 18), background="lightskyblue").grid(column=0, row=4,
                                                                                            sticky=tk.W)
    passb = Entry(f6, show='*')
    passb.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)


    # showpass = Button(text="Show").grid(column=3,row=4, sticky=tk.E,padx=5,pady=5)

    def my_upd(e):  # triggered on select event
        print(cal.get_date())  # read and display


    # # l1=tk.Label(f6,bg='yellow')  # Label to display date
    # # l1.pack()
    # # #lname.pack(pady=10)

    # sal = Label(f6, text="Salary :", font=('arial', 9), background="lightskyblue")
    # sal.grid(column=0,row=5,sticky=tk.W)
    # #sal.pack()

    # salary = DoubleVar()
    # Entry(f6,textvariable=salary).grid(column=1,row=5,sticky=tk.E)
    # print(salary.get())

    # #button_login

    # cal.bind('<<DateEntrySelected>>',my_upd)

    f6.pack()


    def on_closing():
        if askokcancel("Quit", "Do you want to quit?"):
            root.destroy()


    def insdb(cb1,firstname,lastname,mypass,ldate,sec):
        try:
            a = ''.join(random.choices(string.ascii_lowercase, k=10))
            # print(a)
            eid = gen_id(setsec(cb1))
            if eid == None:
                showerror(title="Signup Error",message="Invalid Department")
            else:
                print(eid)

                global emp
                emp = Employee(eid, firstname=firstname, lastname=lastname, password=mypass, dob=ldate, sect=sec,
                            key=a)
                emp.show_info()
                signup_backend(emp.id, emp.firstname, emp.lastname, emp.password, emp.sect, dob=cal.get(),key=emp.key)
                m2fa(a, emp.firstname, "College-Management",cb1)

                # cursor.execute('INSERT INTO login1(emp_id,fname,lname,password,sec,date,key)VALUES (?, ?, ?, ?, ?, ?, ?) ',(emp.id, emp.firstname, emp.lastname, emp.password, emp.sect, emp.dob, emp.key))
            conn.commit()  # Don't forget to commit the changes to the database
        except Exception as e:
            showwarning(title="Error", message="Database error")
            print(e)


    def m2fa(key, name, issuer,cb1):
        uri = pyotp.totp.TOTP(key).provisioning_uri(name=name, issuer_name=issuer)
        # print(uri)
        qrcode.make(uri).save("totp.png")
        win = Toplevel()
        win.geometry("650x650")
        win.config(bg="lightskyblue")
        canvas = Canvas(win, width=470, height=470,bg='lightskyblue')
        canvas.grid(row=2, column=0)
        img = PhotoImage(file="totp.png")
        canvas.create_image(10, 10, anchor=NW, image=img)

        emp_lab = Label(win, text="Emp NO :", font=('arial', 8),bg='lightskyblue').grid(row=4, column=0)
        emp_nolab = Label(win, text=emp.id,bg='green',font=('arial',10)).grid(row=5, column=0)
        note = Label(win,text="Note :[+] Please Notedown your Emp_id for login\n"
                              "[+] Scan for 2 Factor Authentication",bg='yellow').grid(row=3,column=0)

        win.mainloop()


    nb.add(f5, text="Sign up")


    # #basic information
    # def insdb(cb1,firstname,lastname,mypass,ldate,sec):
    #     try:
    #         a = ''.join(random.choices(string.ascii_lowercase, k=10))
    #         # print(a)
    #         eid = gen_id(setsec(cb1))
    #         if eid == None:
    #             showerror(title="Signup Error",message="Invalid Department")
    #         else:
    #             print(eid)
    #             emp = Employee(eid, firstname=firstname, lastname=lastname, password=mypass, dob=ldate, sect=sec,
    #                         key=a)
    #             emp.show_info()
    #             m2fa(a, emp.firstname, "College-Management",cb1)
    #             signup_backend(emp.id, emp.firstname,emp.lastname, emp.password, emp.sect, emp.sect, emp.key)
    #             # cursor.execute('INSERT INTO login1(emp_id,fname,lname,password,sec,date,key)VALUES (?, ?, ?, ?, ?, ?, ?) ',(emp.id, emp.firstname, emp.lastname, emp.password, emp.sect, emp.dob, emp.key))
    #         conn.commit()  # Don't forget to commit the changes to the database
    #     except Exception as e:
    #         showwarning(title="Error", message="Database error")
    #         print(e)
    def signup(event=None):  # Pass event as a default parameter
        firstname = fname.get()
        lastname = lname.get()
        mypass = passb.get()
        ldate = cal.get()
        # salari = salary.get()
        sec = cb1.get()
        if sec == "Admission":
            sect = "AD"
        elif sec == "Fee":
            sect = "FE"
        elif sec == "Exam":
            sect = "EX"
        elif sec == "Library":
            sect = "LIB"
        elif sec == "Faculty":
            sect = "FAC"
        # else:
        #     showerror(title='Failed',message="Signup Failed : Invalid Department")
        insdb(cb1,firstname,lastname,mypass,cal.get(),sec)
        # try:
        #     a = ''.join(random.choices(string.ascii_lowercase, k=10))
        #     # print(a)
        #     emp = Employee(gen_id(setsec(cb1)), firstname=firstname, lastname=lastname, password=mypass, dob=ldate, sect=sec,
        #                 key=a)
        #     emp.show_info()
        #     m2fa(a, emp.firstname, "College-Management")
        #     # query = '''INSERT INTO login1(emp_id,fname,lname,password,sec,date,key)
        #     #             VALUES (?, ?, ?, ?, ?, ?, ?) 
        #     #             '''
        #     # my_data = (emp.id, emp.firstname, emp.lastname, emp.password, emp.sect, emp.dob, emp.key)
        #     cursor.execute('INSERT INTO login1(emp_id,fname,lname,password,sec,date,key)VALUES (?, ?, ?, ?, ?, ?, ?) ',(emp.id, emp.firstname, emp.lastname, emp.password, emp.sect, emp.dob, emp.key))
        #     conn.commit()  # Don't forget to commit the changes to the database
        # except Exception as e:
        #     showwarning(title="Error", message="Database error")





    btn2 = Button(f6, text="Signup", font=('arial', 15), pady=3, command=signup)
    btn2.grid(column=1, row=8, sticky=tk.W, padx=105, pady=5)
    f6.bind('<Return>', signup)
    btn2.bind(signup)
    # def show(key):
    #     print('\nYou Entered {0}'.format(key))
    #     if key == Key.enter:
    #         login()

    root.protocol("WM_DELETE_WINDOW", on_closing)
except Exception as e:
    showwarning(title="Error", message=f"Error : {str(e)}")

root.mainloop()

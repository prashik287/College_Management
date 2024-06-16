from tkinter import *
import tkinter.messagebox
import random
import os
# import Std_info_BackEnd
from tkinter import ttk

import admin_Backend
from mymodules.stdgen import stdgen
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfile
from tkinter import Canvas
from PIL import Image, ImageTk
from tkinter.ttk import Treeview
from tkinter.messagebox import showinfo, showerror
import threading
import time
import Facinfo_Backend
import email_validator
from email_validator import validate_email,EmailNotValidError
class Fac_info():
    def __init__(self, master):
        self.master = master
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.master.title('Admin Section')
        self.master.geometry(f'{self.screen_width}x{self.screen_height}')
        self.master.config(bg='navajowhite')

        def information():
            # ========================================================Variables=====================================================================
            self.empid = StringVar()
            self.Qualification = StringVar()
            self.Experience = IntVar()
            self.position = StringVar()
            self.salary = DoubleVar()
            self.department = StringVar()
            self.pic = bytes()
            # self.profile = StringVar()
            profile = 'profile1.png'

            # ==========================================================Functions====================================================================
            def StudentRec(event):
                try:
                    global selected_tuple
                    index = self.table.selection()[0]
                    selected_tuple = self.table.item(index)['values']
                    print(selected_tuple)
                    self.Entry_std_id.delete(0, END)
                    self.Entry_std_id.insert(END, selected_tuple[1])
                    self.Entry_name.delete(0, END)
                    self.Entry_name.insert(END, selected_tuple[1])
                    self.Entry_department.insert(END, selected_tuple[8])
                except IndexError:
                    pass




            def setprofile():
                if os.path.isfile('user.png'):
                    self.profile = 'user.png'
                else:
                    self.profile = 'profile1.png'
                self.image = Image.open(self.profile)
                resize_img = self.image.resize((90, 90))
                self.img = ImageTk.PhotoImage(resize_img)
                self.canvas.create_image(10, 10, anchor=NW, image=self.img)
            def Display():
                for row in self.table.get_children():
                    self.table.delete(row)
                for row in Facinfo_Backend.view():
                    self.table.insert(parent='', index=0, values=row)
                selected_items = self.table.selection()
                if selected_items:
                    selectedItem = selected_items[0]
                    print(self.table.item(selectedItem)['values'])
                    a = self.table.item(selectedItem)['values']
                    print(a[0])

            def Exit():
                Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
                if Exit > 0:
                    self.master.destroy()
                    return

            def Reset():
                self.empid.set('')
                self.Qualification.set('')
                self.position.set('')
                self.department.set('')
                try:
                    os.remove('user.png')
                except FileNotFoundError as e:
                    print("User Image not found")
                setprofile()

                # self.pic.set('')
                for row in self.table.get_children():
                    self.table.delete(row)

            def Delete():
                # if(len(self.name.get()) != 0):
                #    selectedItem = self.table.selection()[0]
                Facinfo_Backend.delete(self.empid.get())
                # for row in self.table.get_children():
                #        if self.table.item(row)['values'][0] == self.id.get():
                #         print("Deleted")
                #         Std_info_BackEnd.delete(id=self.id.get())
                #         self.table.delete(row)
                #        else:
                #          print("Record Not Found")
                Reset()
                Display()

            def insertb():
                for row in self.table.get_children():
                    # print(row)
                    print(self.table.item(row)['values'][0])
                    self.Entry_std_id.delete(0, END)
                    self.Entry_std_id.insert(END, self.table.item(row)['values'][0])
                    print(self.table.item(row)['values'][1])
                    self.Entry_name.delete(0, END)
                    self.Entry_name.insert(END, self.table.item(row)['values'][6])
                    # self.Entry_fname.delete(0, END)
                    # self.Entry_fname.insert(END, self.table.item(row)['values'][7])
                    # self.Entry_mname.delete(0, END)
                    # self.Entry_mname.insert(END, self.table.item(row)['values'][4])
                    # self.Entry_address.delete(0, END)
                    # self.Entry_address.insert(END, self.table.item(row)['values'][11])
                    # self.Entry_mobno.delete(0, END)
                    # self.Entry_mobno.insert(END, self.table.item(row)['values'][9])
                    # self.Entry_emailID.delete(0, END)
                    # self.Entry_emailID.insert(END, self.table.item(row)['values'][10])
                    # self.Entry_dob.delete(0, END)
                    # self.Entry_dob.insert(END, self.table.item(row)['values'][5])
                    self.Entry_department.delete(0, END)
                    self.Entry_department.insert(END, self.table.item(row)['values'][3])
                    self.Entry_salary.delete(0, END)
                    self.Entry_salary.insert(END, self.table.item(row)['values'][12])
                    self.Entry_post.delete(0, END)
                    self.Entry_post.insert(END, self.table.item(row)['values'][4])


            def Search():
                global a
                for row in self.table.get_children():
                    self.table.delete(row)
                try:
                    for row in admin_Backend.search(self.empid.get()):
                            self.table.insert(parent='', index=0, values=row)
                            print(row)
                    insertb()
                    a = Facinfo_Backend.getimage(self.empid.get())

                    try:
                            with open('user.png', 'wb') as f:
                                f.write(a)
                            setprofile()
                    except Exception as e:
                        showerror(title="Error ",message={e})

                except Exception as e:
                    print(f"Error Occured 1 : {e}")
                    if (str(e) == 'list index out of range'):
                        showerror(title="Not Found", message="Requested Record not exists")

                # self.Entry_name.delete(0,END)
                # self.Entry_name.insert(END,)

            def Update():
                for row in self.table.get_children():
                    self.table.delete(row)
                    self.table.insert(parent='', index=0, values=(
                  self.Qualification.get(),self.department.get(),self.salary.get(),self.position.get(),))
                print(self.Qualification.get())
                admin_Backend.update(empid=self.empid.get(), Salary=self.salary.get(), position=self.position.get())

            def upload_file():
                try:
                    sk = askopenfile(title='Select Image', filetypes=[("Image File", "*.png"), ("All files", '*.*')])
                    with open(sk.name, 'rb') as pp:
                        self.pic = pp.read()
                        # print(self.pic)
                    print("Succesful")
                except Exception as e:
                    print(e)
                def Delete():
                    try:
                        admin_Backend.delete(self.empid.get())
                    except Exception as e:
                        print(e)

            # ============================================================Frames=====================================================================

            self.Main_Frame = LabelFrame(self.master, width=1300, height=100, font=('arial', 20, 'bold'), \
                                         bg='navajowhite', bd=15, relief='ridge')
            self.Main_Frame.grid(row=0, column=0, padx=10, pady=20)

            self.Frame_1 = LabelFrame(self.Main_Frame, width=600, height=20, font=('arial', 15, 'bold'), \
                                      relief='ridge', bd=10, bg='navajowhite', text='Faculty INFORMATION ')
            self.Frame_1.grid(row=1, column=0, padx=10)

            self.Frame_2 = LabelFrame(self.Main_Frame, width=750, height=500, font=('arial', 15, 'bold'), \
                                      relief='ridge', bd=10, bg='navajowhite', text='Faculty DATABASE')
            self.Frame_2.grid(row=1, column=1, padx=5)

            self.Frame_3 = LabelFrame(self.master, width=1200, height=1500 , font=('arial', 10, 'bold'), \
                                      bg='navajowhite', relief='ridge', bd=20)
            self.Frame_3.grid(row=2, column=0, pady=50)
            self.Frame_4 = LabelFrame(self.Frame_2, width=2500, height=100, font=('arial', 15, 'bold'), \
                                      relief='ridge', bd=10, bg='navajowhite', text='Image')
            self.Frame_4.grid(row=0, column=0, pady=10)

            # ========================================================Labels of Frame_1========================================================
            self.Label_std_id = Label(self.Frame_1, text='Faculty id', font=('arial', 20, 'bold'), bg='navajowhite')
            self.Label_std_id.grid(row=0, column=0, sticky=W, padx=20, pady=10)
            self.Label_name = Label(self.Frame_1, text='Qualification', font=('arial', 20, 'bold'), bg='navajowhite')
            self.Label_name.grid(row=1, column=0, sticky=W, padx=20, pady=10)
            # self.Label_fname = Label(self.Frame_1, text='Experience', font=('arial', 20, 'bold'), bg='navajowhite')
            # self.Label_fname.grid(row=2, column=0, sticky=W, padx=20)
            # self.Label_mname = Label(self.Frame_1, text='Position', font=('arial', 20, 'bold'), bg='navajowhite')
            # self.Label_mname.grid(row=3, column=0, sticky=W, padx=20)
            # self.Label_address = Label(self.Frame_1, text='Address', font=('arial', 20, 'bold'), bg='navajowhite')
            # self.Label_address.grid(row=4, column=0, sticky=W, padx=20)
            # self.Label_mobno = Label(self.Frame_1, text='Mobile Number', font=('arial', 20, 'bold'), bg='navajowhite')
            # self.Label_mobno.grid(row=5, column=0, sticky=W, padx=20)
            # self.Label_emailID = Label(self.Frame_1, text='Email ID', font=('arial', 20, 'bold'), bg='navajowhite')
            # self.Label_emailID.grid(row=6, column=0, sticky=W, padx=20)
            # self.Label_dob = Label(self.Frame_1, text='Date of Birth', font=('arial', 20, 'bold'), bg='navajowhite')
            # self.Label_dob.grid(row=7, column=0, sticky=W, padx=20)
            self.Label_department = Label(self.Frame_1, text='Department', font=('arial', 20, 'bold'), bg='navajowhite')
            self.Label_department.grid(row=8, column=0, sticky=W, padx=20, pady=10)
            self.Label_salary = Label(self.Frame_1,text="Salary", font=('arial', 20, 'bold'), bg='navajowhite')
            self.Label_salary.grid(row=9, column=0, sticky=W, padx=20, pady=10)
            self.Label_post = Label(self.Frame_1,text="Job Title", font=('arial', 20, 'bold'), bg='navajowhite')
            self.Label_post.grid(row=10, column=0, sticky=W, padx=20, pady=10)
            # self.Label_gender = Label(self.Frame_1, text='Gender', font=('arial', 20, 'bold'), bg='navajowhite')
            # self.Label_gender.grid(row=9, column=0, sticky=W, padx=20, pady=10)

            # ========================================================Entries of Frame_1========================================================
            self.Entry_std_id = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.empid)
            # self.Entry_std_id.insert(0, "For  search update and \n delete only")
            self.Entry_std_id.grid(row=0, column=1, padx=10, pady=5)
            self.Entry_name = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.Qualification)
            self.Entry_name.grid(row=1, column=1, padx=10, pady=5)
            # self.Entry_fname = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.Experience)
            # self.Entry_fname.grid(row=2, column=1, padx=10, pady=5)
            # self.Entry_mname = ttk.Combobox(self.Frame_1, values=(
            # ' ', 'HOD','Lecturer'), \
            #                                      font=('arial', 17, 'bold'), textvariable=self.position, width=19)
            # self.Entry_mname.grid(row=3, column=1, padx=10, pady=5)
            # self.Entry_address = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.address)
            # self.Entry_address.grid(row=4, column=1, padx=10, pady=5)
            # self.Entry_mobno = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.mobno)
            # self.Entry_mobno.grid(row=5, column=1, padx=10, pady=5)
            # self.Entry_emailID = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.email)
            # self.Entry_emailID.grid(row=6, column=1, padx=10, pady=5)
            # # self.Entry_dob = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.dob)
            # self.Entry_dob = DateEntry(self.Frame_1, selectmode='day', year=2020, month=5, day=22,
            #                            font=('arial', 17, 'bold'), textvariable=self.dob)
            # self.Entry_dob.grid(row=7, column=1, padx=10, pady=5)
            self.Entry_department = ttk.Combobox(self.Frame_1, values=(
            ' ', 'Information Technology', 'Computer Science', 'Cybersecurity', 'Mechanical', 'Civil', 'Chemical'), \
                                                 font=('arial', 17, 'bold'), textvariable=self.department, width=19)
            self.Entry_department.grid(row=8, column=1, padx=10, pady=5)

            self.Entry_post = ttk.Combobox(self.Frame_1, values=(
            ' ', 'HOD', 'Lecturer'), font=('arial', 17, 'bold'), textvariable=self.position, width=19)
            self.Entry_post.grid(row=10, column=1, padx=10, pady=5)
            self.Entry_salary = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.salary)
            self.Entry_salary.grid(row=9,column=1,padx=10,pady=5)

            # self.Entry_gender = ttk.Combobox(self.Frame_1, values=(' ', 'Male', 'Female', 'Others'), \
            #                                  font=('arial', 17, 'bold'), textvariable=self.gender, width=19)
            # self.Entry_gender.grid(row=9, column=1, padx=10, pady=5)

            # ========================================================Buttons of self.Frame_3=========================================================
            # self.btnSave = Button(self.Frame_3, text='SAVE', font=('arial', 17, 'bold'), width=8, command=Add)
            # self.btnSave.grid(row=0, column=0, padx=10, pady=10)
            self.btnDisplay = Button(self.Frame_3, text='DISPLAY', font=('arial', 17, 'bold'), width=8, command=Display)
            self.btnDisplay.grid(row=0, column=1, padx=10, pady=10)
            self.btnReset = Button(self.Frame_3, text='RESET', font=('arial', 17, 'bold'), width=8, command=Reset)
            self.btnReset.grid(row=0, column=2, padx=10, pady=10)
            self.btnUpdate = Button(self.Frame_3, text='UPDATE', font=('arial', 17, 'bold'), width=8, command=Update)
            self.btnUpdate.grid(row=0, column=3, padx=10, pady=10)
            self.btnDelete = Button(self.Frame_3, text='DELETE', font=('arial', 17, 'bold'), width=8, command=Delete)
            self.btnDelete.grid(row=0, column=4, padx=10, pady=10)
            self.btnSearch = Button(self.Frame_3, text='SEARCH', font=('arial', 17, 'bold'), width=8, command=Search)
            self.btnSearch.grid(row=0, column=5, padx=10, pady=10)
            self.btnExit = Button(self.Frame_3, text='EXIT', font=('arial', 17, 'bold'), width=8, command=Exit)
            self.btnExit.grid(row=0, column=6, padx=10, pady=10)

            # ===============================================List Box and self.scrollbar========================================================
            # self.scrollbar = Scrollbar(self.Frame_2)
            # self.scrollbar.grid(row = 2, column = 2, sticky = 'ns')

            # self.listbox = Listbox(self.Frame_2, width = 75, height = 5 , font = ('arial',12,'bold'))
            # self.listbox.bind('<<ListboxSelect>>', StudentRec)
            # self.listbox.grid(row = 2, column = 0)
            # self.scrollbar.config(command = self.listbox.yview)
            self.table = Treeview(self.Frame_2, columns=(
            'Faculty_id', 'First_Name', 'Last_name','Department', 'Position', 'Join_date',  'Qualification', 'exp','Gender',
            'mobno','Email','address'), show=('headings'))

            self.table.heading('Faculty_id', text='Faculty id')
            self.table.heading('First_Name', text='First Name')
            self.table.heading('Last_name', text='Last Name')
            self.table.heading('Department', text='Department')
            self.table.heading('Position', text='Job Title')
            self.table.heading('Join_date', text='Join Date')
            # self.table.heading('salary', text='Salary')
            self.table.heading('Gender', text='Gender')
            self.table.heading('Qualification', text='Qualification')
            self.table.heading('exp', text='Experience')
            self.table.heading('mobno', text='Mobile No')
            self.table.heading('Email',text='Email')
            self.table.heading('address',text='Address')
            self.table.grid(row=3, column=0, sticky='ns')
            self.table.column('Faculty_id', width=80)
            self.table.column('First_Name', width=80)
            self.table.column('Last_name', width=80)
            self.table.column('Department', width=100)
            self.table.column('Position', width=80)
            self.table.column('Join_date', width=80)
            # self.table.column('salary', width=80)
            self.table.column('Gender', width=80)
            self.table.column('Email',width=80)
            self.table.column('Qualification', width=80)
            self.table.column('exp', width=70)
            self.table.column('mobno', width=80)
            self.table.column('address',width=80)
            # ==============================================IMage==================================================================================
            # self.btnfile = Button(self.Frame_2, text="Change  Image", command=upload_file)
            # self.btnfile.grid(column=0, row=2, padx=1, pady=10)
            self.canvas = Canvas(self.Frame_4, width=100, height=100)
            self.canvas.grid(row=0, column=0)

            # if os.path.isfile('user.png'):
            #       profile = 'profile1.png'
            # else:


        information()


root = Tk()
obj = Fac_info(root)
root.mainloop()

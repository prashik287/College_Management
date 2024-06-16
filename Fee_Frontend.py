import sqlite3
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import datetime
import Fee_Backend
import createreceipt
from tkinter.ttk import Treeview
from tkinter.messagebox import showerror
from random import randint
import tkinter as tk
import phonenumbers
class Fee():
    def __init__(self, master):
        self.master = master
        self.master.title('Fee Report')
        self.master.geometry('1350x750')
        self.master.config(bg='Navajo white')

        # ==================================================Variables=================================================
        self.recpt = IntVar()
        self.name = StringVar()
        # self.admsn = StringVar()
        self.date = StringVar()
        self.branch = StringVar()
        self.sem = StringVar()
        self.total = DoubleVar()
        self.paid = DoubleVar()
        self.due = DoubleVar()
        self.method = StringVar()
        self.drawnon = StringVar()
        self.amountw = StringVar()

        # ==================================================Functions=================================================
        def Tuple(event):
            try:
                global st
                index = self.table.selection()[0]
                st = self.table.item(index)['values']
                print(st)
                self.recpt_entry.delete(0, END)
                self.recpt_entry.insert(END, st[1])
                self.name_entry.delete(0, END)
                self.name_entry.insert(END, st[2])
                # self.admsn_entry.delete(0, END)
                # self.admsn_entry.insert(END, st[3])
                self.Date_entry.delete(0, END)
                self.Date_entry.insert(END, st[4])
                self.branch_entry.delete(0, END)
                self.branch_entry.insert(END, st[5])
                self.sem_entry.delete(0, END)
                self.sem_entry.insert(END, st[6])
                self.total_entry.delete(0, END)
                self.total_entry.insert(END, st[7])
                self.paid_entry.delete(0, END)
                self.paid_entry.insert(END, st[8])
                self.due_entry.delete(0, END)

                self.due_entry.insert(END, st[9])
            except IndexError:
                pass

        def Insert():
            # if (len(self.admsn.get()) != 0):
            try:

                Fee_Backend.insert(recpt=self.recpt.get(),name= self.name.get(), date=self.date.get(),
                                   branch=self.branch.get(), year1=self.sem.get(),method= self.method.get(), paid=self.paid.get(),
                                   due=self.due.get(),drawnon=self.drawnon.get(),words=self.amountw.get())
            except sqlite3.IntegrityError as e:
                showerror(title="Integrity Error",message="An Error Occured")


                # self.list.insert(END, (self.recpt.get(), self.name.get(), self.admsn.get(), self.date.get(),
                #                        self.branch.get(), self.sem.get(), self.total.get(), self.paid.get(),
                #                        self.due.get()))

        def insertb():
            for row in self.table.get_children():
                # print(row)
                print(self.table.item(row)['values'][0])
                self.recpt_entry.delete(0, END)
                self.recpt_entry.insert(END, self.table.item(row)['values'][0])
                print(self.table.item(row)['values'][1])
                self.name_entry.delete(0, END)
                self.name_entry.insert(END, self.table.item(row)['values'][1])
                self.Date_entry.delete(0, END)
                self.Date_entry.insert(END, self.table.item(row)['values'][2])
                self.branch_entry.delete(0, END)
                self.branch_entry.insert(END, self.table.item(row)['values'][3])
                self.sem_entry.delete(0, END)
                self.sem_entry.insert(END, self.table.item(row)['values'][4])
                self.total_entry.delete(0, END)
                self.total_entry.insert(END, self.table.item(row)['values'][5])
                self.method_entry.delete(0, END)
                self.method_entry.insert(END, self.table.item(row)['values'][5])
                self.paid_entry.delete(0, END)
                self.paid_entry.insert(END, self.table.item(row)['values'][7])
                self.drawn_entry.delete(0, END)
                # if self.table.item(row)['values'][9] == " ":
                #     self.drawn_entry.configure(state=tk.DISABLED)
                # else:
                self.drawn_entry.insert(END, self.table.item(row)['values'][9])
                self.due_entry.delete(0, END)
                self.due_entry.insert(END, self.table.item(row)['values'][8])
                self.amountw_entry.delete(0,END)
                # self.amountw_entry.insert(END,self.table.item(row)['values'[10]])

        def View():
            # Clear all existing rows from the treeview
            for row in self.table.get_children():
                self.table.delete(row)

            # Retrieve rows from the backend and insert them into the treeview
            for row in Fee_Backend.view():
                self.table.insert(parent='', index='end', values=row)
                print(row)

        def Reset():
            self.recpt.set(' ')
            self.recpt_entry.configure(state=tk.NORMAL)
            self.name.set(' ')
            # self.admsn.set(' ')
            self.amountw.set('')
            #self.date.set(' ')
            self.branch.set(' ')
            self.sem.set(' ')
            self.paid.set(0.0)  
            self.due.set(0.0)
            normal_ever()
            self.Display.delete('1.0', END)
            for row in self.table.get_children():
                self.table.delete(row)

        def Delete():
            Fee_Backend.delete(self.recpt.get())
            Reset()
            View()
        def printre():
            try:
                # gen_rec()
                createreceipt.printreceipt( std_name=self.name.get(),receipt_no=self.recpt.get(),amount_in_words=self.amountw.get(),paid=self.paid.get(),balance=self.due.get(),clas=self.sem.get(),depart=self.branch.get(),method=self.method.get(),drawn=self.drawnon.get())
            except Exception as e:
                print(e)
        def Receipt():
                self.Display.delete('1.0', END)
                self.Display.insert(END, '\t\tRECEIPT' + '\n\n')
                self.Display.insert(
                    END, '\tReceipt No.\t     :' + str(self.recpt.get()) + '\n')
                self.Display.insert(END, '\tStudent Name  :' +
                                    self.name.get() + '\n')
                self.Display.insert(END, '\tAdmission No.\t:' +
                                    '\n')
                self.Display.insert(
                    END, '\tDate\t          :' + self.date.get() + '\n')
                self.Display.insert(
                    END, '\tBranch\t          :' + self.branch.get() + '\n')
                self.Display.insert(
                    END, '\tSemester \t        :' + self.sem.get() + '\n\n')
                x3 = self.due_entry.get()
                print(x3)
                x2 = self.paid_entry.get()  # Initialize x2 to 0
                x1 = self.total_entry.get()
                if float(x3) == 0.0:
                    x4 = (float(x1) - float(x2))
                    # print("IF block")
                else:
                    x4 = (float(x3) - float(x2))
                    print(x4)

                self.Display.insert(END, '\tTotal Amount  :' + str(x1) + '\n')
                self.Display.insert(END, '\tPaid Amount   :' + str(x2) + '\n')
                self.Display.insert(END, '\tBalance\t         :' + str(x4) + '\n')
                self.due_entry.delete(0,END)
                self.due_entry.insert(END, x4)

                # self.due.set(x3)
        def disable_ever():
                self.recpt_entry.config(state='disabled')
                self.name_entry.config(state='disabled')
                self.branch_entry.config(state='disabled')
                self.Date_entry.config(state='disabled')
                # self.due_entry.config(state='disabled')
                self.sem_entry.config(state='disabled')
        def normal_ever():
                self.name_entry.config(state='normal')
                self.branch_entry.config(state='normal')
                self.Date_entry.config(state='normal')
                self.due_entry.config(state='normal')
                self.sem_entry.config(state='normal')
                
        def Search():
           
            for row in self.table.get_children():
                self.table.delete(row)

            for row in Fee_Backend.search(self.recpt.get()):
                self.table.insert(parent='',index=0, values=row)
                insertb()
            disable_ever()

            

        def Update():
            Fee_Backend.update(self.recpt.get(),self.paid_entry.get(),self.due_entry.get(),self.drawn_entry.get())
            

        def Exit():
            Exit = tkinter.messagebox.askyesno(
                'Attention', 'Confirm, if you want to Exit')
            if Exit > 0:
                root.destroy()
                return
        def detect_selected(event):
            if self.method_entry.get() == 'DD':
                self.drawn_entry.config(state='normal')
            else:
                self.drawn_entry.config(state='disabled')
        # ==================================================Frames===================================================
        Main_Frame = Frame(self.master, bg='Navajo white')
        Main_Frame.grid()

        Title_Frame = LabelFrame(
            Main_Frame, width=1350, height=100, bg='Navajo white', relief='ridge', bd=15)
        Title_Frame.pack(side=TOP)

        self.lblTitle = Label(Title_Frame, font=('arial', 40, 'bold'), text='FEE REPORT',
                              bg='navajowhite', padx=13)
        self.lblTitle.grid(padx=400)

        Data_Frame = Frame(Main_Frame, width=1350, height=350,
                           bg='Navajo white', relief='ridge', bd=15)
        Data_Frame.pack(side=TOP, padx=15)

        Frame_1 = LabelFrame(Data_Frame, width=850, height=350, bg='Navajo white', relief='ridge', bd=8,
                             text='Informations', font=('arial', 15, 'bold'))
        Frame_1.pack(side=LEFT, padx=10)

        Frame_2 = LabelFrame(Data_Frame, width=495, height=350, bg='Navajo white', relief='ridge', bd=8,
                             text='Fee Receipt', font=('arial', 15, 'bold'))
        Frame_2.pack(side=RIGHT, padx=10)

        List_Frame = Frame(Main_Frame, width=1350, height=150,
                           bg='Navajo white', relief='ridge', bd=15)
        List_Frame.pack(side=TOP, padx=15)

        Button_Frame = Frame(Main_Frame, width=1350, height=80,
                             bg='Navajo white', relief='ridge', bd=15)
        Button_Frame.pack(side=TOP)

        # ===================================================Labels================================================
        self.recpt_label = Label(Frame_1, text='Receipt No. : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.recpt_label.grid(row=0, column=0, padx=15, sticky=W)

        self.name_label = Label(Frame_1, text='Student Name : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.name_label.grid(row=1, column=0, padx=15, sticky=W)

        # self.admsn_label = Label(Frame_1, text='Admission No. : ', font=(
        #     'arial', 14, 'bold'), bg='Navajo white')
        # self.admsn_label.grid(row=2, column=0, padx=15, sticky=W)

        self.Date_label = Label(Frame_1, text='Date : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.Date_label.grid(row=3, column=0, padx=15, sticky=W)

        self.branch_label = Label(Frame_1, text='Branch : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.branch_label.grid(row=4, column=0, padx=15, sticky=W)

        self.sem_label = Label(Frame_1, text='Year : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.sem_label.grid(row=5, column=0, padx=15, sticky=W)
        self.amountw_label = Label(Frame_1, text='Amount in words : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.amountw_label.grid(row=0, column=2, padx=5, sticky=W)
        self.drawn_label = Label(Frame_1, text='Drawn on : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.drawn_label.grid(row=1, column=2, padx=5, sticky=W)
        self.method_label = Label(Frame_1, text='Payment Method : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.method_label.grid(row=2, column=2, padx=5, sticky=W)
        self.total_label = Label(Frame_1, text='TOTAL AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.total_label.grid(row=3, column=2, padx=5, sticky=W)

        self.paid_label = Label(Frame_1, text='PAID AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.paid_label.grid(row=4, column=2, padx=5, sticky=W)

        self.due_label = Label(Frame_1, text='BALANCE : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.due_label.grid(row=5, column=2, padx=5, sticky=W)

        # ==================================================Entries=================================================
        self.var_1 = DoubleVar(Frame_1, value='36265')
        d1 = datetime.date.today()
        self.date.set(d1)

        self.recpt_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.recpt)
        self.recpt_entry.grid(row=0, column=1, padx=15, pady=5)

        self.name_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.name)
        self.name_entry.grid(row=1, column=1, padx=15, pady=5)

        # self.admsn_entry = Entry(Frame_1, font=(
        #     'arial', 14), textvariable=self.admsn)
        # self.admsn_entry.grid(row=2, column=1, padx=15, pady=5)

        self.Date_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.date)
        self.Date_entry.grid(row=3, column=1, padx=15, pady=5)

        self.branch_entry = ttk.Combobox(Frame_1, values=(' ', 'CSE', 'IT', 'ETC/ET&T', 'Mechanical', 'Civil', 'EE', 'EEE'),
                                         font=('arial', 14), width=19, textvariable=self.branch)
        self.branch_entry.grid(row=4, column=1, padx=15, pady=5)

        self.sem_entry = ttk.Combobox(Frame_1, values=(' ', 'FSE', 'SE', 'DSE', 'TE', 'FY'), font=('arial', 14), width=19,
                                      textvariable=self.sem)
        self.sem_entry.grid(row=5, column=1, padx=15, pady=5)

        self.total_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.var_1, state='readonly')
        self.total_entry.grid(row=3, column=3, padx=8, pady=5)
        self.method_entry = ttk.Combobox(Frame_1, values=( 'DD','Cash', 'Online'),
                                         font=('arial', 14), width=19, textvariable=self.method)
        self.method_entry.grid(row=2, column=3, padx=15, pady=5)
        self.amountw_entry = Entry(Frame_1, font=(
            'arial', 14), width=20, textvariable=self.amountw)
        self.amountw_entry.grid(row=0, column=3, pady=5)
        self.drawn_entry = Entry(Frame_1, font=(
            'arial', 14), width=20, textvariable=self.drawnon)
        self.drawn_entry.grid(row=1, column=3, pady=5)
        self.paid_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.paid)
        self.paid_entry.grid(row=4, column=3, pady=5)

        self.due_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.due)
       
        self.due_entry.grid(row=5, column=3, pady=7)

        # ==================================================Frame_2=================================================
        self.Display = Text(Frame_2, width=42, height=12,
                            font=('arial', 14, 'bold'))
        self.Display.grid(row=0, column=0, padx=3)

        # =============================================List box and scrollbar===========================================
        sb = Scrollbar(List_Frame)
        sb.grid(row=0, column=1, sticky='ns')
        self.method_entry.bind('<<ComboboxSelected>>',detect_selected)
        #
        # self.list = Listbox(List_Frame, font=(
        #     'arial', 13, 'bold'), width=140, height=8)
        # self.list.bind('<<ListboxSelect>>', Tuple)
        # self.list.grid(row=0, column=0)
        # sb.config(command=self.list.yview)
        #===============================================================================================================
        self.table = Treeview(List_Frame,
                              columns=('receipt_no', 'Name', 'date', 'branch','year','method','total','paid','balance','drawn' ), show=('headings'))

        self.table.heading('receipt_no', text='Receipt No')
        self.table.heading('Name', text='Name')
        self.table.heading('date', text='Date')
        self.table.heading('branch', text='Branch')
        # self.table.heading('sem', text='Semester')
        self.table.heading('year', text='Year')
        self.table.heading('method', text='Payment Method')
        self.table.heading('total', text='Total Amount')
        self.table.heading('paid', text='Paid')
        self.table.heading('balance', text='Balance')
        self.table.heading('drawn',text='Drawn on')

        self.table.grid(row=0, column=0, sticky='ns')
        self.table.column('receipt_no', width=80)
        self.table.column('Name', width=80)
        self.table.column('date', width=80)
        self.table.column('branch', width=80)
        self.table.heading('method', text='Payment Method')
        self.table.column('total', width=80)
        self.table.column('paid', width=80)
        self.table.column('balance', width=80)

        # self.table.column('address', width=100)

        def gen_rec():
            random_number = randint(1111, 9999)
            self.recpt_entry.delete(0, tk.END)  # Clear existing content
            self.recpt_entry.insert(tk.END, random_number)

            paid_amount_str = self.paid_entry.get()
            due_amount_str = self.due_entry.get()

            if not paid_amount_str.strip():
                showerror(title="ValueError", message=f"Please enter a valid paid amount.")
                return

            if not due_amount_str.strip():
                showerror(title="ValueError", message=f"Please enter a valid due amount.")
                return

            paid_amount = float(paid_amount_str)
            due_amount = float(due_amount_str)

            if paid_amount <= due_amount:
                Receipt()
            elif paid_amount > 0:
                Receipt()
            else:
                showerror(title="ValueError", message=f"Please enter a valid amount.")
        # ==================================================Buttons=================================================
        btnSave = Button(Button_Frame, text='SAVE', font=(
            'arial', 14, 'bold'), width=10, command=Insert)
        btnSave.grid(row=0, column=0, padx=5, pady=5)

        btnDisplay = Button(Button_Frame, text='DISPLAY', font=(
            'arial', 14, 'bold'), width=10, command=View)
        btnDisplay.grid(row=0, column=1, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='RESET', font=(
            'arial', 14, 'bold'), width=10, command=Reset)
        btnReset.grid(row=0, column=2, padx=5, pady=5)

        btnUpdate = Button(Button_Frame, text='UPDATE', font=(
            'arial', 14, 'bold'), width=10, command=Update)
        btnUpdate.grid(row=0, column=3, padx=5, pady=5)

        btnSearch = Button(Button_Frame, text='SEARCH', font=(
            'arial', 14, 'bold'), width=10, command=Search)
        btnSearch.grid(row=0, column=4, padx=5, pady=5)

        btnDelete = Button(Button_Frame, text='DELETE', font=(
            'arial', 14, 'bold'), width=10, command=Delete)
        btnDelete.grid(row=0, column=5, padx=5, pady=5)

        btnReceipt = Button(Button_Frame, text='RECEIPT', font=(
            'arial', 14, 'bold'), width=10, command=gen_rec)
        btnReceipt.grid(row=0, column=6, padx=5, pady=5)
        btnPrint = Button(Button_Frame, text='Print', font=(
            'arial', 14, 'bold'), width=10, command=printre)
        btnPrint.grid(row=0, column=7, padx=5, pady=5)

        btnExit = Button(Button_Frame, text='EXIT', font=(
            'arial', 14, 'bold'), width=10, command=Exit)
        btnExit.grid(row=0, column=8, padx=5, pady=5)


root = Tk()
obj = Fee(root)
root.mainloop()

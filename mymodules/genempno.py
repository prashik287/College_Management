from random import randint
from tkinter.messagebox import showinfo,showerror
def gen_id(dept):
    if dept == None:
        b=dept
    else:
        a = randint(1001,2001)
        b = f"{dept}{a}"
    return b


class Employee:
    def __init__(self,emp_id,firstname,lastname,password,dob ,key,sect):
        self.id = emp_id
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.dob = dob
        self.sect = sect
        self.key = key


    def show_info(self):
        print(f"Employee ID : {self.id}\n First Name : {self.firstname}\n Last Name : {self.lastname}\n  Section:{self.sect}")
        showinfo(f"Success","Your Empid is ".format(self.id)+str(self.id))
# emp1 = Employee(gen_id("FAC"),"Dev","Kumar","kali","21/05/2005",)
# emp1.show_info()





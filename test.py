# # # # import os
# # # # import threading
# # # # def get_file():
# # # #     while True:
# # # #        if os.path.exists('user.png'):
# # # #               print('profile1')
# # # #        else:
# # # #               print('profile2')
# # #
# # # # t1 = threading.Thread(target=get_file)
# # #
# # # # if __name__ == '__main__':
# # # #        t1.start()
# # #
# # # # from email_validator import *
# # # #
# # # # email = 'prashikj17@gmail'
# # # # try:
# # # #     emailinfo = validate_email(email,check_deliverability=True)
# # # # except EmailNotValidError as e:
# # # #     print("Invalid Email")
# # #
# # # # import phonenumbers
# # # #
# # # # num = '+917738216810'
# # # # mynum = phonenumbers.parse(num)
# # # # print(phonenumbers.is_valid_number(mynum))
# # #
# # # # import sqlite3
# # # # # from Std_info_BackEnd import searchndp
# # # # # #
# # # # # conn = sqlite3.connect("fee.db")
# # # # # cur = conn.cursor()
# # # # # # # name = "Prashik Jadhav"
# # # # # recpt =4894902
# # # # # cur.execute("SELECT * FROM fee WHERE  recpt = ?",
# # # # #             (recpt,))
# # # # #
# # # # # rows = cur.fetchall()
# # # # # print(rows)
# # #
# # # from mymodules.genempno import Employee,gen_id
# # #
# # # class Faculty(Employee,):
# # #     def __init__(self,emp_id,firstname,lastname,password,join_date ,key,sect):
# # #         self.id = emp_id
# # #         self.firstname = firstname
# # #         self.lastname = lastname
# # #         self.password = password
# # #         self.join_date= join_date
# # #         self.sect = sect
# # #         self.key = key
# # #         self.salary
# # #         self.experience
# # #         self.qualification
# # #         self.position
# # #         self.pic
# # #     def set_info(self,salary,experience,qualification,posisition,pic):
# # #         self.salary = salary
# # #         self.experience =experience
# # #         self.qualification =qualification
# # #         self.position = posisition
# # #         self.pic =pic
# # import datetime
# # import time
# #
# # print(datetime.datetime.now())
# # # #
# # import os

# # print(os.path.isfile('Facinfo_Frontend.py '))
# # #
# # #
# # #
# # #
# # #
# # #
# # import aspose.pdf as ap
# # # Instantiate an object of HtmlLoadOptions
# # options = ap.HtmlLoadOptions()
# # # Convert HTML to PDF
# # document = ap.Document("index.html", options)
# # # Save PDF
# # document.save("output.pdf")
# import sqlite3
# try:
#     conn = sqlite3.connect('college.db')
#     cursor = conn.cursor()
#     cursor.execute('Select due from fee where recpt = 1767')
#     a = cursor.fetchall()
#     for i in a:
#         print(i[0])

# except Exception as e:
#     print(f"Failed to connect to database:{e}")
# num = float(input("Enter Float value: "))
# if num < 0:
#     print("Negative")
# import sqlite3
# con = sqlite3.connect('college.db')
# cur = con.cursor()

# cur.execute('Select paid from fee where recpt = ?', (9749,))
# pai = cur.fetchall()
# print(float(pai[0][0]))
#
# x =1.34
#
# print(isinstance(x,float))
# import phonenumbers
# # x = phonenumbers.parse("+91773821680",None)
# # print(phonenumbers.is_valid_number(x))
# a = ['r','a','j','e']
# a = ['r','a','j','e']
# for i, e in zip(a, range(1, 10)):
#     print(i, e)

import phonenumbers
# phonenumbers.parse("917738216810")
num = "+917738216810"
num1=phonenumbers.parse(num)
print(phonenumbers.is_valid_number(num1))
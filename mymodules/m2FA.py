# import pyotp
# import qrcode
# from tkinter import Toplevel
# from tkinter import Canvas
# from tkinter import *
# from PIL import Image, ImageTk
# # from setsec import setsec
# from mymodules.setsec import setsec
# from mymodules.genempno import gen_id

# def m2fa(key, name, issuer,cb1):
#         uri = pyotp.totp.TOTP(key).provisioning_uri(name=name, issuer_name=issuer)
#         # print(uri)
#         qrcode.make(uri).save("totp.png")
#         win = Toplevel()
#         win.geometry("650x650")
#         win.config(bg="lightskyblue")
#         canvas = Canvas(win, width=470, height=470,bg='lightskyblue')
#         canvas.grid(row=1, column=0)
#         img = PhotoImage(file="totp.png")
#         canvas.create_image(10, 10, anchor=NW, image=img)
#         emp_lab = Label(win, text="Emp NO :", font=('arial', 8),bg='lightskyblue').grid(row=2, column=0)
#         emp_nolab = Label(win, text=gen_id(dept=setsec(cb1)),bg='green',font=('arial',10)).grid(row=3, column=0)
#         note = Label(win,text="Note :[+] Please Notedown your Emp_id for login\n"
#                               "[+] Scan for 2 Factor Authentication",bg='yellow').grid(row=3,column=0)

# # key = "abcdefghijklmnop"
# # name = "John Doe"
# # issuer = "Acme Inc."
# # cb1 = "IT"
# # m2fa(key, name, issuer, cb1)
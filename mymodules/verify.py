import pyotp
import sqlite3
import qrcode
from tkinter.simpledialog import askinteger
import subprocess





# def gen_qr(key):
#     uri = pyotp.totp.TOTP(key).provisioning_uri(name="Prashik", issuer_name="Datta Meghe")
#     print(uri)
#     qrcode.make(uri).save("totp.png")

def verify():
    totp = pyotp.TOTP("qmnhrpmfyt")
    # print(totp.now())
    otp = input('Enter the OTP: ')
    
    if totp.verify(otp):
        print("successful")
    else:
        print("unsuccessful")

verify()



from tkinter import *
from tkinter import filedialog
from tkinter import Label

root = Tk()
root.geometry('1500x700')
root.title("Tutorial")
s1 = Label(root,text='Selected File:')
s1.pack()
s2 = Label(root,text='')
s2.pack()
s3 = Label(root,text='')
s3.pack()


def open_file():
    try:
        filepath = filedialog.askopenfile(title='Select Image',filetypes=[("Image File","*.png"),("All files",'*.*')])
        s2.config(text=f"{filepath.name}")
        process_file(filepath.name)
    except Exception as e:
        print(e)
def process_file(filename):
    with open(filename,"rb") as f:
        filecontent = f.read()
        s3.config(text=f'{filecontent}')
b1 = Button(root,text="Select File",command=open_file)
b1.pack()
root.mainloop()
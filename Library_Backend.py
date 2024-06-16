import sqlite3

def connect():
       con = sqlite3.connect('college.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS library(x INTEGER PRIMARY KEY, Mtype text, refno integer, fname text, \
                     surname text, address text, post integer, mobno integer, ID text, title text, author text, \
                     borrow integer, due integer, loan integer)')


       con.commit()
       con.close()

def insert(Mtype = ' ', refno = ' ', fname = ' ', surname = ' ', address = ' ', post = ' ', mobno = ' ', ID = ' ', \
           title = ' ', author = ' ', borrow = ' ', due = ' ', loan = ' '):
       con = sqlite3.connect('college.db')
       cur = con.cursor()

       cur.execute('INSERT INTO library VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)',(Mtype,refno,fname,surname,address,post, \
                                                                                  mobno,ID,title,author,borrow,due,loan))

       con.commit()
       con.close()

def view():
       con = sqlite3.connect('college.db')
       cur = con.cursor()

       cur.execute('SELECT Mtype,refno,fname,surname,address,post,mobno,ID,title,author,borrow,due,loan FROM library')
       row = cur.fetchall()
       return row

       con.close()
def delete(x):
       con = sqlite3.connect('college.db')
       cur = con.cursor()

       cur.execute('DELETE FROM library WHERE x = ?',(x,))
       
       con.commit()
       con.close()
       
def update(x, Mtype = ' ', refno = ' ', fname = ' ', surname = ' ', address = ' ', post = ' ', mobno = ' ', ID = ' ', \
           title = ' ', author = ' ', borrow = ' ', due = ' ', loan = ' '):
       con = sqlite3.connect('college.db')
       cur = con.cursor()

       cur.execute('UPDATE library SET Mtype = ? , fname = ? ,surname = ? , address = ?, post = ?,mobno = ? , ID = ? OR title = ? OR author = ? OR borrow = ? OR due = ? OR loan = ?',(Mtype,refno,fname,surname,address, post,mobno,ID,title,author,borrow,due,loan))
       con.commit()
       con.close()

def search(refno):
       con = sqlite3.connect('college.db')
       cur = con.cursor()

       cur.execute('SELECT Mtype,refno,fname,surname,address,post,mobno,ID,title,author,borrow,due,loan FROM library WHERE  refno = ? ',(refno,))
       row = cur.fetchall()
       return row
       con.close()


connect()
       
       
       
                   
       

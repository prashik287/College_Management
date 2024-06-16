import sqlite3
from tkinter.messagebox import showerror

def connect():
       con = sqlite3.connect('college.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS fee(recpt integer PRIMARY KEY, name1 text NOT NULL, date1 text NOT NULL, \
                    branch text NOT NULL, year1 text NOT NULL,payment_method text NOT NULL ,total REAL DEFAULT 36265, paid REAL NOT NULL, due REAL NOT NULL DEFAULT 1, drawnon text DEFAULT "-",amount_words text NOT NULL)')

       con.commit()
       con.close()

def insert(recpt = ' ', name = ' ', date = ' ', branch = ' ', year1 = ' ',method='', total = ' ', paid = ' ', due = ' ',drawnon='',words=''):
       con = sqlite3.connect('college.db')
       cur = con.cursor()

       cur.execute('INSERT INTO fee(recpt,name1,date1,branch,year1,payment_method,paid,due,drawnon,amount_words) VALUES (?,?,?,?,?,?,?,?,?,?)',(recpt,name,date,branch,year1,method,paid,due,drawnon,words))

       con.commit()
       con.close()

def view():
       con = sqlite3.connect('college.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM fee')
       row = cur.fetchall()
       return row

       con.commit()
       

def delete(recpt=''):
       try:
              con = sqlite3.connect('college.db')
              cur = con.cursor()

              cur.execute('DELETE  FROM fee WHERE recpt = ?',(recpt,))

              con.commit()
              con.close()
       except Exception as e:
              print(e)

def update(recpt=' ', paid=' ', due=' ', drawnon=''):
    con = sqlite3.connect('college.db')
    cur = con.cursor()
    cur.execute('Select paid from fee WHERE recpt = ?',(recpt,))
    c = cur.fetchall()
#     print(c[0][0])
    n = c[0][0]
    finalpaid = n + float(paid)
#     print(f'{a[0]} is received value')

    cur.execute('UPDATE fee SET paid = ?, due = ?, drawnon = ? WHERE recpt = ?', (finalpaid, due, drawnon, recpt))
    a = cur.fetchall()
    for i in a:
           print(a)
    con.commit()

    con.close()

def search(recpt =''):
       con = sqlite3.connect('college.db')
       cur = con.cursor()

       cur.execute("SELECT * FROM fee WHERE  recpt = ?",
                   (recpt,))
       row = cur.fetchall()
       return row

       con.commit()
       
connect()



import sqlite3

def connect():
       conn = sqlite3.connect("college.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS student (stdid text PRIMARY KEY, recpt INT NOT NULL,name text NOT NULL, fname text NOT NULL, mname text NOT NULL,department text NOT NULL, \
                     address text NOT NULL, mobno integer NOT NULL,email text NOT NULL, dob integer NOT NULL, gender text NOT NULL,img BLOP NOT NULL,\
                     foreign key(recpt) references  'fee' on delete cascade)")

       conn.commit()
       conn.close()

def insert(stdid=" ",recept='' ,name = " ", fname = " ", mname = " ", department ='',address = " ", mobno = " ", email = " ", dob = " ", gender = " ",img=""):
       conn = sqlite3.connect("college.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO student VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (stdid,recept,name, fname, mname, department,address , mobno, email, dob, gender,img))

       conn.commit()
       conn.close()
                                                                        

def view():
       conn = sqlite3.connect("college.db")
       cur = conn.cursor()

       cur.execute("SELECT student.stdid,student.recpt,student.name,student.fname,student.mname,student.address,student.mobno,student.email,student.dob,student.gender,student.department FROM student LEFT JOIN fee ON student.recpt=fee.recpt")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(id):
       conn = sqlite3.connect("college.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM student WHERE stdid = ?", (id,))

       conn.commit()
       conn.close()

def update(id='', name='', fname='', mname='',address='', mobno='', email='', dob='', gender='', pic=''):
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()

    cur.execute("""
                UPDATE student
                SET name = ?, fname = ?, mname = ?, address = ?, mobno = ?, email = ?, dob = ?, gender = ?, img = ?
                WHERE stdid = ?
                """, (name, fname, mname, address, mobno, email, dob, gender, pic, id))

    conn.commit()
    conn.close()


def search(id =""):
       conn = sqlite3.connect("college.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM student WHERE stdid = ?  ", (id,))
       rows = cur.fetchall()

       return rows
       
       conn.close()


# def searchndp(name='',department=''):
#     conn = sqlite3.connect("college.db")
#     cur = conn.cursor()
#     # name = "Prashik Jadhav"
#     cur.execute("SELECT stdid,name,fname,mname,address,mobno,email,dob,gender,department FROM student WHERE  name == ? and department == ?",
#                 (name,department))
#     rows = cur.fetchall()
#     print(rows)
#     return rows

    # conn.close()
# def search_namedep(name='',fname='',department=''):
#        try:
#               conn = sqlite3.connect("college.db")
#               cur = conn.cursor()

#               cur.execute("SELECT * FROM student WHERE name = ? and fname = ? and department = ? ", (name,fname,department,))
#               rows = cur.fetchall()

#               return rows
#        except Exception as e:
#               print('Database error')
              
       # conn.close()
def getimage(stdid):
       # global i
       conn = sqlite3.connect('college.db')
       cursor = conn.cursor()
       a = cursor.execute('Select img from student where stdid == ?',(stdid,))
       n = a.fetchall()[0][0]
       # print(a.fetchone())
       return n                                               
connect()
       

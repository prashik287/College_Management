import sqlite3


def connect():
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()

    cur.execute(""" CREATE TABLE IF NOT EXISTS Faculty1 (empid TEXT PRIMARY KEY, Qualification TEXT NOT NULL,Experience INTEGER NOT NULL,position TEXT NOT NULL,Salary REAL NOT NULL,join_date TEXT NOT NULL,address TEXT NOT NULL,mobno INTEGER NOT NULL,email TEXT NOT NULL,dob TEXT NOT NULL,gender TEXT NOT NULL,    department TEXT NOT NULL,img BLOB NOT NULL,   FOREIGN KEY (empid) REFERENCES login1(empid) ON DELETE CASCADE)""")

    conn.commit()
    conn.close()

def insert(empid=" ",  qualification=" ", Experience=" ", position='',join_date=" ", address=" ", mobno=" ", email=" ", dob=" ", gender=" ",
           department=" ", img=""):
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO Faculty1 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (empid,  qualification, Experience,position,30000,join_date, address, mobno, email, dob, gender, department, img))

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()

    cur.execute("Select Faculty1.empid,login1.fname,login1.lname,Faculty1.department,Faculty1.position,login1.date,Faculty1.Qualification,Faculty1.Experience,Faculty1.gender,Faculty1.mobno,Faculty1.email,Faculty1.address from Faculty1 left join login1 ON login1.emp_id=Faculty1.empid")
    rows = cur.fetchall()
    return rows

    conn.close()


def delete(id):
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM Faculty1 WHERE empid = ?", (id,))

    conn.commit()
    conn.close()


def update(empid='', Qualification='', Experience='', address='', mobno='', email='', dob='', gender='', pic=''):
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()

    cur.execute("""
                UPDATE Faculty1
                SET Qualification = ?, Experience = ?,  address = ?, mobno = ?, email = ?, dob = ?, gender = ?, img = ?
                WHERE empid = ?
                """, (Qualification, Experience,  address, mobno, email, dob, gender, pic, empid))

    conn.commit()
    conn.close()


def search(empid="",):
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()

    cur.execute("Select Faculty1.empid,login1.fname,login1.lname,Faculty1.department,Faculty1.position,login1.date,Faculty1.Qualification,Faculty1.Experience,Faculty1.gender,Faculty1.mobno,Faculty1.email,Faculty1.address from Faculty1 left join login1 ON login1.emp_id=Faculty1.empid WHERE login1.emp_id == ? ",
                (empid,))
    rows = cur.fetchall()

    return rows

    conn.close()


def searchndp(name='', department=''):
    conn = sqlite3.connect("college.db")
    cur = conn.cursor()
    # name = "Prashik Jadhav"
    cur.execute(
        "SELECT stdid,name,fname,mname,address,mobno,email,dob,gender,department FROM student WHERE  name == ? and department == ?",
        (name, department))
    rows = cur.fetchall()
    print(rows)
    return rows

    conn.close()


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
def getimage(empid):
    # global i
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    a = cursor.execute('Select img from Faculty1 where empid == ?', (empid,))
    n = a.fetchall()[0][0]
    # print(a.fetchone())
    return n


connect()


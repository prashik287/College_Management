import sqlite3
def connect():
    conn = sqlite3.connect('college.db')
    # cursor = conn.cursor()
    return  conn

def search(empid=''):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("Select Faculty1.empid,login1.fname,login1.lname,Faculty1.department,Faculty1.position,login1.date,Faculty1.Qualification,Faculty1.Experience,Faculty1.gender,Faculty1.mobno,Faculty1.email,Faculty1.address,Faculty1.Salary from  Faculty1 LEFT join login1 ON login1.emp_id=Faculty1.empid ")
    a = cursor.fetchall()
    return  a

def update(empid='', Salary='', position=''):
    try:
        conn=connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE Faculty1 SET Salary = ?, position = ? WHERE empid = ?",
                       (Salary, position, empid))
        conn.commit()

    except Exception as e:
        print(e)
def delete(empid=''):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Faculty1 where empid = ?",(empid,))
    except Exception as e:
        print(e)

def getimage(empid):
    # global i
    conn = connect()
    cursor = conn.cursor()
    a = cursor.execute('Select img from Faculty1 where empid == ?', (empid,))
    n = a.fetchall()[0][0]
    # print(a.fetchone())
    return n

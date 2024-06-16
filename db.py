import sqlite3
conn = sqlite3.connect("college.db")
cursor = conn.cursor()
# a = cursor.execute("Select * from sqlite_master")
# for i in a.fetchall():
#     print(i)
#cursor.execute("CREATE TABLE IF NOT EXISTS login1(emp_id TEXT PRIMARY KEY,fname TEXT,lname TEXT,password TEXT, sec TEXT, date TEXT,key TEXT)")
# cursor.execute("INSERT INTO login values('Loki','Asguard@123','Admission')")
b = cursor.execute("SELECT * FROM login1")
for i in b.fetchall():
    print(i)
# b = cursor.execute("Select password from login where username == 'charlie' AND SECTION == 'Admission'")
# for i in b.fetchall():
#     print(i[0])
conn.commit()
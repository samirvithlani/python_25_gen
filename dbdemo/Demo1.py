import sqlite3

#connect to database
con = sqlite3.connect("school.db")

#cursor object

cur = con.cursor()


#create table
cur.execute("""
CREATE TABLE IF NOT EXISTS STUDENT
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
marks REAL)""")

con.commit()

#insert query

# cur.execute("insert into student(name,age,marks)values(?,?,?)",("ram",22,98.5))
# cur.execute("insert into student(name,age,marks)values(?,?,?)",("jay",21,66.5))
#con.commit()

cur.execute("select * from student")
#cur.execute("select * from student where name = ?",("ram",))
students = cur.fetchall()
#students = cur.fetchone()
#students = cur.fetchmany(1)
print(students)
print(min(students,key=lambda x:x[3]))
con.commit()

#update record:
# cur.execute("update student set marks =? where name = ?",(88.88,"priya"))
# con.commit()


#cur.execute("DELETE from student where name =?",("ram",))
#con.commit()
con.close()



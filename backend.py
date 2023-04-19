import sqlite3

def connect():
    conn=sqlite3.connect("Employee.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS emp (id INTEGER PRIMARY KEY, Ename text, Eid text, contact big int(10),Address text,mailid varchar(20))")
    conn.commit()
    conn.close()

def insert(Ename,Eid,contact,Address,mailid):
    conn=sqlite3.connect("Employee.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO emp VALUES (NULL,?,?,?,?,?)",(Ename,Eid,contact,Address,mailid))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("Employee.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM emp")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(Ename="",Eid="",contact="",Address="",mailid=""):
    conn=sqlite3.connect("Employee.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM emp WHERE Ename=? OR Eid=? OR contact=? OR Address=? or mailid=?", (Ename,Eid,contact,Address,mailid))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("Employee.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM emp WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,Ename,Eid,contact,Address,mailid):
    conn=sqlite3.connect("Employee.db")
    cur=conn.cursor()
    cur.execute("UPDATE emp SET Ename=?, Eid=?, contact=?, Address=?, mailid=? WHERE id=?",(Ename,Eid,contact,Address,mailid,id))
    conn.commit()
    conn.close()

connect()
#insert("The Sun","John Smith",1918,"913123132",)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
print(view())
#print(search(author="John Smooth"))

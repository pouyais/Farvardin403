import sqlite3


class Database:
    def __init__(self,path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS contact(id integer PRIMARY KEY, fname text, lname text, address text, phone integer)")
        self.con.commit()

    def insert(self,fname,lname,address,phone):
        self.cur.execute("INSERT INTO contact VALUES (NULL, ?, ?, ?, ?)",(fname,lname,address,phone))
        self.con.commit()

    def remove(self,id):
        self.cur.execute("DELETE FROM contact WHERE id = ?",(id,))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM contact")
        rows = self.cur.fetchall()
        return rows
    
    def update(self,id,fname,lname,address,phone):
        self.cur.execute("UPDATE contact SET fname = ?, lname = ?, address = ?, phone = ? WHERE id = ?",(fname,lname,address,phone,id))
        self.con.commit()

    def search(self,name):
        self.cur.execute("SELECT * FROM contact WHERE id = ? or fname = ? or lname = ? or address = ? or phone = ?",(name,name,name,name,name))
        recs = self.cur.fetchall()
        return recs
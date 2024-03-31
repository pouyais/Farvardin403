import sqlite3


class Database:
    def __init__(self,path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS products(id integer PRIMARY KEY, name text, buyprice float, sellprice float, quantity integer)")
        self.con.commit()

    def insert(self,product,buyprice,sellprice,quantity):
        self.cur.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?)",(product,buyprice,sellprice,quantity))
        self.con.commit()

    def remove(self,id):
        self.cur.execute("DELETE FROM products WHERE id = ?",(id,))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM products")
        rows = self.cur.fetchall()
        return rows
    
    def update(self,id,prodcut,buyprice,sellprice,quantity):
        self.cur.execute("UPDATE products SET name = ?, buyprice = ?, sellprice = ?, quantity = ? WHERE id = ?",(prodcut,buyprice,sellprice,quantity,id))
        self.con.commit()

    def search(self,name):
        self.cur.execute("SELECT * FROM products WHERE id = ? or name = ? or buyprice = ? or sellprice = ? or quantity = ?",(name,name,name,name,name))
        recs = self.cur.fetchall()
        return recs
import sqlite3 as sql

def create_database():

        with sql.connect("website_msg0.db") as con:
            cur = con.cursor()
            con = sql.connect('website_msg0.db')
            cur.execute('CREATE TABLE IF NOT EXISTS  message (name TEXT, post TEXT)')
            con.commit()
            con.close()



def save_rec(name,post):
    with sql.connect("website_msg0.db") as con:
      cur = con.cursor()
      con = sql.connect('website_msg0.db')
      cur.execute("INSERT INTO message(name,post) VALUES(?, ?)", (name, post))
      con.commit()
      con.close()
    msg = "Record successfully added"
    return msg
def retrive():
    with sql.connect("website_msg0.db") as con:
        cur = con.cursor()
        con = sql.connect("website_msg0.db")
        con.row_factory = sql.Row
        cur.execute("select * from message")
        rows = cur.fetchall()
        return rows
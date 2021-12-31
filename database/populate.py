import database as db
import sqlite3
import pandas as pd


class InsertData:
    
    def __init__(self):
        self.conn = sqlite3.connect(db.FULLNAME)
        self.cur = self.conn.cursor()
    
    def populate(self, insert_values):
        query = """INSERT INTO {} (doc, page, doc_text) VALUES(?,?,?);""".format(db.TABLE)
        self.cur.executemany(query, insert_values)
        self.conn.commit()   

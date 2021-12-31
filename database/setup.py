from pathlib import Path
import database as db
import sqlite3
import pandas as pd


class NewDataBase:
    
    def __init__(self):
        
        if not Path(db.DIR).is_dir():
            print('create folder for database: {}'.format(db.LOCATION))
            Path.mkdir(db.LOCATION)
            
        self.conn = sqlite3.connect(db.FULLNAME)
        self.cur = self.conn.cursor()
        
    def create(self):
        query = """CREATE VIRTUAL TABLE IF NOT EXISTS {} USING fts5 (doc, page, doc_text)""".format(db.TABLE)
        self.cur.execute(query)

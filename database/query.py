import database as db
import sqlite3
import pandas as pd
import re


class FullTextSearch:
    
    def __init__(self):
        self.conn = sqlite3.connect(db.FULLNAME)
        self.cur = self.conn.cursor()
        
    def query(self, search_term):
        query = """SELECT * FROM {}
                   WHERE doc_text MATCH '{}'
                   ORDER BY rank;
                """.format(db.TABLE, self._term_processing(search_term))
        try:
            result = self._format_result(pd.read_sql(query, self.conn))
        except:
            result = pd.DataFrame()
        return result 
    
    def _term_processing(self, term):
        pattern = '"([\w\s\.]*)"'
        results = re.findall(pattern, term)
        term = re.sub('"([\w\s\.]*)"|(\w+)', lambda match: match.group(1) or match.group(2) + '*', term)

        for quote in results:
            quote_ = '"' + quote + '"'
            term = re.sub(quote, quote_, term, count=1)

        for pattern in [["AND[*]", "AND"], ["OR[*]", "OR"], ["NOT[*]", "NOT"]]:
            term = re.sub(pattern[0], pattern[1], term)
            
        term = re.sub('-', ' ', term)
        print('searching results for {}'.format(term))
        return term
    
    def _format_result(self, result):    
        mask = result.groupby('doc')
        df = mask.aggregate(lambda x: tuple(x)[:10])
        df = df.reset_index()
        
        df['new'] = df[['doc', 'page']].values.tolist()
        df['page'] = df['new']
        
        df = df.drop(columns=['doc_text'])
        df = df.drop(columns=['new'])
        
        col1 = "found in document"
        col2 = "found on pages"
        df = df.rename(columns={"doc": col1, "page": col2})
        
        cont_col1 = lambda x: '<a href="{}" target="_blank">{}</a>'.format(re.sub(str(db.PDFFILE), db.PDF, x),re.sub(str(db.PDFFILE),'', x))
        
        def page_links(var): 
            pdf_link = re.sub(str(db.PDFFILE), db.PDF, str(var[0]))
            clickit = ''
            for page in var[1]:
                if page == 0:
                    if len(var[1]) <= 1: 
                        clickit += '<a href="{}" target="_blank">{}</a> '.format(pdf_link, 'doc')
                else:
                    clickit += '<a href="{}" target="_blank">{}</a> '.format(pdf_link+'#page='+str(page), page)
            return clickit

        cont_col2 = lambda x: page_links(x)
        df = df.style.format(formatter={(col1): cont_col1, (col2): cont_col2})
        return df
    
class RegisteredPDF:
    
    def __init__(self):
        self.conn = sqlite3.connect(db.FULLNAME)
        self.cur = self.conn.cursor()
        
    def query(self):
        query = "SELECT doc FROM {};".format(db.TABLE)
        return pd.read_sql(query, self.conn).doc.tolist()
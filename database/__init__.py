from pathlib import Path

BASEDIR = Path(__file__).resolve().parent.parent
with open(BASEDIR / 'pdf_fts.conf', 'r') as f:
    content = f.read().splitlines()  
    
_vars = {}
for item in content:
    if '#' in item:
        pass
    else:
        if '=' in item:
            key_val = item.split('=')
            _vars[str(key_val[0])] = str(key_val[1])
    
DIR = _vars['DIR']
NAME = _vars['NAME'] 
TABLE = _vars['TABLE']
PDF = _vars['PDF']
PDFFILE = BASEDIR / PDF

LOCATION = BASEDIR / DIR
FULLNAME = str(LOCATION / NAME)

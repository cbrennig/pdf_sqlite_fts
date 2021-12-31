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

LANG = _vars['LANG']
DPI = int(_vars['DPI'])
FMT = _vars['FMT']
GRAYSCALE = bool(_vars['GRAYSCALE'])
IMGFMT = _vars['IMGFMT']
CONFIG = _vars['CONFIG']

TEMPPATH = BASEDIR / _vars['TEMP']
PDFPATH = BASEDIR / _vars['PDF']

import filemanager as fm
from pathlib import Path


class TempImages:
    
    def __init__(self):
        pass
        
    def _delete(self):
        print('remove all temporary image files from folder {}'.format(fm.TEMPPATH)) 
        
        for file in [file for file in sorted(Path(fm.TEMPPATH).glob('*.jpg'))]:
            Path(file).unlink()
        
import filemanager as fm
from pathlib import Path


class Folders:
    
    def __init__(self):
        pass
    
    def _setup_pdf(self):
        if not Path(fm.PDFPATH).is_dir():
            print('folder {} will be created'.format(fm.PDFPATH))
            Path.mkdir(fm.PDFPATH)
        else:
            print('folder {} already exists'.format(fm.PDFPATH))
        return True
            
    def _setup_img(self):
        if not Path(fm.TEMPPATH).is_dir():
            print('folder {} will be created'.format(fm.TEMPPATH))
            Path.mkdir(fm.TEMPPATH)
        else:
            print('folder {} already exists'.format(fm.TEMPPATH))
        return True

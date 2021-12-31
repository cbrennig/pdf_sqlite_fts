import filemanager as fm
from pathlib import Path


class CheckPDF:
    
    def __init__(self):
        self.pdf_new = []
        self.pdf_all = []
        self.pdf_registered = []
        
    def status_pdf(self):
        print('check pdf files in {}'.format(fm.PDFPATH))
        counter = 0
        for file in [file for file in sorted(Path(fm.PDFPATH).glob('*.pdf'))]: 
            self.pdf_all.append(fm.PDFPATH / file)
            if str(fm.PDFPATH / file) not in self.pdf_registered:
                self.pdf_new.append(file)
                counter += 1
        print('... {} new pdf files found.'.format(counter))
    
    
class CheckImages:
    
    def __init__(self):
        self.img_all = []
        
    def status_img(self):
        print('get all image files in {}'.format(fm.TEMPPATH))
        
        for file in [file for file in sorted(Path(fm.TEMPPATH).glob('*.jpg'))]: 
            self.img_all.append(fm.TEMPPATH / file)
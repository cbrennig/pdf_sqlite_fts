import convert as ct
import pytesseract
import multiprocessing
from multiprocessing import Pool
import os

class OCR:
    def __init__(self):
        self.cpus = multiprocessing.cpu_count()
        os.environ["OMP_THREAD_LIMIT"] = "1"

    def _recognise_text(self, page):
        print('.', end='')
        return [str(page[0]), page[1], pytesseract.image_to_string(str(page[2]), lang=ct.LANG, config=ct.CONFIG)]
    
    def get_text(self, list_of_images):
        print('start ocr from {} pages'.format(len(list_of_images))) 
        p = Pool(self.cpus)
        #return self._fulldoc_text(p.map(self._recognise_text, list_of_images))
        #return p.map(self._recognise_text, list_of_images)
        return self._fulldoc_text(p.map(self._recognise_text, list_of_images))
            
    def _fulldoc_text(self, text):
        allpages = ''
        for page in text:
            allpages += page[2]
            
        text.append([str(page[0]), 0, allpages])
        return text 
        

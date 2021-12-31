import convert as ct
from pdf2image import convert_from_path
import numpy as np
import cv2

class ConvertPDF:
    
    def __init__(self):
        self.new_converted_pdf = []
    
    def picturise(self, file):
        pdf = ct.PDFPATH  / file
        images = convert_from_path(pdf,
                               dpi=ct.DPI,
                               fmt=ct.FMT,
                               grayscale=ct.GRAYSCALE)
        
        for i, image in enumerate(images):
            pagenum = i+1
            filename = str(pagenum) + '.' + ct.IMGFMT
            imagefile = ct.TEMPPATH / filename       
            img = np.array(image)
            (thresh, img_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            cv2.imwrite(str(imagefile), img_bw)
            
            self.new_converted_pdf.append([pdf, pagenum, imagefile])


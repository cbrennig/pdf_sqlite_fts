from database.query import RegisteredPDF
from database.populate import InsertData
from filemanager.status import CheckPDF, CheckImages
from filemanager.remove import TempImages
from convert.pdf import ConvertPDF
from convert.ocr import OCR

DB_PDF = RegisteredPDF()
ID = InsertData()
CPDF = CheckPDF()

CPDF.pdf_registered = DB_PDF.query()
CPDF.status_pdf()
TEMP = TempImages()
TEMP._delete()

for file in CPDF.pdf_new:
    CONV = ConvertPDF()
    CONV.picturise(file)
    
    text_all_pages = OCR().get_text(CONV.new_converted_pdf)
    ID.populate([tuple(doc) for doc in text_all_pages])
    print('ready')

    TEMP._delete()
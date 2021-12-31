from database.setup import NewDataBase
from filemanager.setup import Folders

F = Folders()
F._setup_pdf()
F._setup_img()

NDB = NewDataBase()
NDB.create()
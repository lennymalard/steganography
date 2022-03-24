from encodage import*
from Stega import *



def connection_encodage(app):
    main(app.encImageLabel.file_path, message = app.encPswdLineEdit.text(), key = app.encMessLineEdit.text())

def connection_decodage(app):
    print(main(app.decImageLabel.file_path,key=app.decPswdLineEdit.text()))

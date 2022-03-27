import sys
import os

path = "E:\\NSI\\projets\\steganography"

os.chdir(path)
sys.path.append(f"{os.getcwd()}\\front-end\\py-files")
sys.path.append(f"{os.getcwd()}\\front-end\\ui-files")
sys.path.append(f"{os.getcwd()}\\back-end")
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import uic
from link import *
from DecryptedDialog import DecryptedDialog
from EncryptedDialog import EncryptedDialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(f"{os.getcwd()}\\front-end\\ui-files\\main.ui", self)

        self.encMessage = ""
        self.decMessage = ""
        self.encKey = ""
        self.decKey = ""

        def eraseAll():
            self.encImageLabel.clear()
            self.decImageLabel.clear()

            self.encImageLabel.is_imported = False
            self.decImageLabel.is_imported = False

            self.encPswdLineEdit.clear()
            self.decPswdLineEdit.clear()

            self.encMessLineEdit.clear()

            self.encPswdLineEdit.setEnabled(False) 

            self.encPswdBtnBox.setEnabled(False)
            self.decPswdBtnBox.setEnabled(False)

            self.encMessBtnBox.setEnabled(False)

            self.runEncBtn.setEnabled(False)
            self.runDecBtn.setEnabled(False)

            self.encImageLabel.setText("ENCRYPT")
            self.decImageLabel.setText("DECRYPT")

        def clickEncryptPageBtn():
            print("opening 'encrypt page'")
            self.stackedWidget.setCurrentWidget(self.encryptPage)
        def clickDecryptPageBtn():
            print("opening 'decrypt page'")
            self.stackedWidget.setCurrentWidget(self.decryptPage)
        def clickMenuPageBtn():
            print("opening 'menu page'")
            eraseAll()
            self.stackedWidget.setCurrentWidget(self.menuPage)

        def clickEncPswdOkBtn():
            print(f"enc key: {self.encPswdLineEdit.text()}")
            self.encKey = self.encPswdLineEdit.text()
            self.runEncBtn.setEnabled(True)
        def clickEncPswdCancelBtn():
            self.encPswdLineEdit.clear()
        def clickDecPswdOkBtn():
            print(f"dec key: {self.decPswdLineEdit.text()}")
            self.decKey = self.decPswdLineEdit.text()
            self.runDecBtn.setEnabled(True)
        def clickDecPswdCancelBtn():
            self.decPswdLineEdit.clear()

        def clickEncMessOkBtn():
            print(f"message: {self.encMessLineEdit.text()}")
            self.encMessage = self.encMessLineEdit.text()
            self.encPswdLineEdit.setEnabled(True)  
        def clickEncMessCancelBtn():
            self.encMessLineEdit.clear()

        def encPswdTextChanged():
            if self.encImageLabel.is_imported == True and self.encPswdLineEdit.text() != "":
                self.encPswdBtnBox.setEnabled(True)
            else:
                self.encPswdBtnBox.setEnabled(False)
        def decPswdTextChanged():
            if self.decImageLabel.is_imported == True and self.decPswdLineEdit.text() != "":
                self.decPswdBtnBox.setEnabled(True)
            else:
                self.decPswdBtnBox.setEnabled(False)

        def encMessTextChanged():
            if self.encImageLabel.is_imported == True and self.encMessLineEdit.text() != "":
                self.encMessBtnBox.setEnabled(True)
            else:
                self.encMessBtnBox.setEnabled(False)

        def clickRunEncBtn():
            print(f"{self.encMessage}, {self.encKey}, {self.encImageLabel.image_path}")
            encoding_link(path=self.encImageLabel.image_path, message=self.encMessage, key=self.encKey)
            self.encKey = ""
            encDialog = EncryptedDialog()
            encDialog.exec_()

        def clickRunDecBtn():
            self.decMessage = decoding_link(path=self.decImageLabel.image_path, message=False, key=self.decKey)
            print(self.decMEssage)
            decDialog = DecryptedDialog()
            decDialog.exec_()

        self.encryptPageButton.clicked.connect(clickEncryptPageBtn)
        self.decryptPageButton.clicked.connect(clickDecryptPageBtn)
        self.menuPageButton.clicked.connect(clickMenuPageBtn)

        self.encPswdBtnBox.accepted.connect(clickEncPswdOkBtn)
        self.encPswdBtnBox.rejected.connect(clickEncPswdCancelBtn)
        self.decPswdBtnBox.accepted.connect(clickDecPswdOkBtn)
        self.decPswdBtnBox.rejected.connect(clickDecPswdCancelBtn)

        self.encMessBtnBox.accepted.connect(clickEncMessOkBtn)
        self.encMessBtnBox.rejected.connect(clickEncMessCancelBtn)

        self.encPswdLineEdit.textChanged.connect(encPswdTextChanged)
        self.decPswdLineEdit.textChanged.connect(decPswdTextChanged)

        self.encMessLineEdit.textChanged.connect(encMessTextChanged)

        self.runEncBtn.clicked.connect(clickRunEncBtn)
        self.runDecBtn.clicked.connect(clickRunDecBtn)
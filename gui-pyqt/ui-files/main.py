import sys 
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import uic

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        def eraseAll():
            self.encImageLabel.clear()
            self.decImageLabel.clear()

            self.encImageLabel.is_imported = False
            self.decImageLabel.is_imported = False

            self.encPswdLineEdit.clear()
            self.decPswdLineEdit.clear()

            self.encPswdBtnBox.setEnabled(False)
            self.decPswdBtnBox.setEnabled(False)

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
            print(f"password: {self.encPswdLineEdit.text()}")
            self.runEncBtn.setEnabled(True)
        def clickEncPswdCancelBtn():
            self.encPswdLineEdit.clear()
        def clickDecPswdOkBtn():
            print(f"password: {self.decPswdLineEdit.text()}")
            self.runDecBtn.setEnabled(True)
        def clickDecPswdCancelBtn():
            self.decPswdLineEdit.clear()

        def encPswdTextChanged():
            if self.encImageLabel.is_imported == True:
                self.encPswdBtnBox.setEnabled(True)
        def decPswdTextChanged():
            if self.decImageLabel.is_imported == True:
                self.decPswdBtnBox.setEnabled(True)

        self.encryptPageButton.clicked.connect(clickEncryptPageBtn)
        self.decryptPageButton.clicked.connect(clickDecryptPageBtn)
        self.menuPageButton.clicked.connect(clickMenuPageBtn)

        self.encPswdBtnBox.accepted.connect(clickEncPswdOkBtn)
        self.encPswdBtnBox.rejected.connect(clickEncPswdCancelBtn)
        self.decPswdBtnBox.accepted.connect(clickDecPswdOkBtn)
        self.decPswdBtnBox.rejected.connect(clickDecPswdCancelBtn)

        self.encPswdLineEdit.textChanged.connect(encPswdTextChanged)
        self.decPswdLineEdit.textChanged.connect(decPswdTextChanged)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("""
        """)
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Application...")

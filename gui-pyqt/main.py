import sys 
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6 import uic

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        def eraseAll():
            self.imageLabel.clear()
            self.imageLabel.is_imported = False
            self.pswdLineEdit.clear()
            self.pswdBtnBox.setEnabled(False)

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
        def clickPswdOkBtn():
            print(f"password: {self.pswdLineEdit.text()}")
        def clickPswdCancelBtn():
            self.pswdLineEdit.clear()

        def pswdTextChanged():
            if self.imageLabel.is_imported == True:
                self.pswdBtnBox.setEnabled(True)

        self.encryptPageButton.clicked.connect(clickEncryptPageBtn)
        self.decryptPageButton.clicked.connect(clickDecryptPageBtn)
        self.menuPageButton.clicked.connect(clickMenuPageBtn)
        self.pswdBtnBox.accepted.connect(clickPswdOkBtn)
        self.pswdBtnBox.rejected.connect(clickPswdCancelBtn)
        self.pswdLineEdit.textChanged.connect(pswdTextChanged)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("""
        """)
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Application...")
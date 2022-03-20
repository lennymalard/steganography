import sys 
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6 import uic

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        def clickEncryptPageBtn():
            print("opening 'encrypt page'")
            self.stackedWidget.setCurrentWidget(self.encryptPage)
        def clickDecryptPageBtn():
            print("opening 'decrypt page'")
            self.stackedWidget.setCurrentWidget(self.decryptPage)
        def clickMenuPageBtn():
            print("opening 'menu page'")
            self.stackedWidget.setCurrentWidget(self.menuPage)
        def clickPswdOkBtn():
            print(f"password: {self.pswdLineEdit.text()}")
        def clickPswdCancelBtn():
            self.pswdLineEdit.clear()

        self.encryptPageButton.clicked.connect(clickEncryptPageBtn)
        self.decryptPageButton.clicked.connect(clickDecryptPageBtn)
        self.menuPageButton.clicked.connect(clickMenuPageBtn)
        self.pswdBtnBox.accepted.connect(clickPswdOkBtn)
        self.pswdBtnBox.rejected.connect(clickPswdCancelBtn)

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
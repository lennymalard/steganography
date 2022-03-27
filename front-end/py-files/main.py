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
from MainWindow import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("""
        """)
    mw = MainWindow()
    mw.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Application...")

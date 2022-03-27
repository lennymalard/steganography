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

class EncryptedDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(f"{os.getcwd()}\\front-end\\ui-files\\encryptedDialog.ui", self)

        self.imagePathLabel.setText(f"{os.getcwd()}")

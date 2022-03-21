from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class imageLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        QtWidgets.QLabel.__init__(self, *args, **kwargs)
        self.is_imported = False

    def dragEnterEvent(self, event):
            if event.mimeData().hasImage:
                event.accept()
            else:
                event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.setPixmap(QtGui.QPixmap(file_path).scaled(self.width(),self.height(), Qt.AspectRatioMode.KeepAspectRatio))
            print(file_path)
            self.is_imported = True
            event.accept()
        else:
            event.ignore()
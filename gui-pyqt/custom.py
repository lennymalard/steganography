from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6.QtCore import Qt

class imageLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        QtWidgets.QLabel.__init__(self, *args, **kwargs)

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
            event.accept()
        else:
            event.ignore()
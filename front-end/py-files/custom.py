from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class ImageLabel(QtWidgets.QLabel):
    """
    Widget personalisé qui permet d'importer une image et de l'afficher.

    attributs :
        -is_imported : permet de savoir si une image est présente ou pas dans le widget.
        -image_path : permet de garder en mémoire le chemin d'accès de l'image.

    methodes :
        -drageEnterEvent 
        -dragMoveEvent
        -dropEvent 
    """
    def __init__(self, *args, **kwargs):
        QtWidgets.QLabel.__init__(self, *args, **kwargs)
        self.is_imported = False
        self.image_path = ""

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
        """
        Affiche l'image une fois importé
        """
        if event.mimeData().hasImage:
            self.image_path = event.mimeData().urls()[0].toLocalFile()
            self.setPixmap(QtGui.QPixmap(self.image_path).scaled(self.width(),self.height(), Qt.AspectRatioMode.KeepAspectRatio))
            print(self.image_path)
            self.is_imported = True
            event.accept()
        else:
            event.ignore()
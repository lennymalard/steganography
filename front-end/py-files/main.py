import sys # module servant à ajouter aux chemins d'accès de python le chemin d'accès du module
import os # mdodule servant à changer de fichier et de récupérer le chemin d'accès du fichier actuel

path = "E:\\NSI\\projets\\steganography" # chemin d'accès du module 

os.chdir(path) # methode permettant de changer fichier
sys.path.append(f"{os.getcwd()}\\front-end\\py-files") # on ajoute le fichier py-files aux chemins d'accès de python
sys.path.append(f"{os.getcwd()}\\front-end\\ui-files") # on ajoute le fichier ui-files aux chemins d'accès de python
sys.path.append(f"{os.getcwd()}\\back-end") # on ajoute le fichier back-end aux chemins d'accès de python
from PyQt5 import QtWidgets # on importe le module QtWidgets, module permettant de créer des widgets
from PyQt5 import uic # on importe le module uic, module permettant d'importer une interface graphique faite à partir du logiciel "Qt Designer"
from MainWindow import MainWindow # on importe le constructeur du widget de la fenetre principale depuis son fichier

if __name__ == '__main__':
    """
    on definit ici les actions devant être éxecuté en lancant le fichier 
    """
    app = QtWidgets.QApplication(sys.argv) # on créé un widget QApplication afin de créer l'application
    app.setStyleSheet(""" # on definit ici une feuille de style vide
        """)
    mw = MainWindow() # on créé un widget "MainWindow" 
    mw.show() # on affiche les éléments inclus dans ce widget

    try:
        sys.exit(app.exec_()) # on affiche et execute le widget dans la boucle globale si tout ce passe bien
    except SystemExit: # sinon on ferme la genêtre principale
        print("Closing Application...")
import sys # module servant à ajouter aux chemins d'accès de python le chemin d'accès du module
import os # mdodule servant à changer de fichier et de récupérer le chemin d'accès du fichier actuel

path = "E:\\NSI\\projets\\steganography" # chemin d'accès du module 

os.chdir(path) # methode permettant de changer fichier
sys.path.append(f"{os.getcwd()}\\front-end\\py-files") # on ajoute le fichier py-files aux chemins d'accès de python
sys.path.append(f"{os.getcwd()}\\front-end\\ui-files") # on ajoute le fichier ui-files aux chemins d'accès de python
sys.path.append(f"{os.getcwd()}\\back-end") # on ajoute le fichier back-end aux chemins d'accès de python
from PyQt5 import QtWidgets # on importe le module QtWidgets, module permettant de créer des widgets
from PyQt5 import uic # on importe le module uic, module permettant d'importer une interface graphique faite à partir du logiciel "Qt Designer"
from link import * # on importe les fonctions permettant le lien entre le front-end et le back-end depuis leur fichier
from DecryptedDialog import DecryptedDialog # on importe le constructeur du widget de la fenêtre de dialogue "DecryptedDialog" depuis son fichier
from EncryptedDialog import EncryptedDialog # on importe le constructeur du widget de la fenêtre de dialogue "EncryptedDialog" depuis son fichier

class MainWindow(QtWidgets.QMainWindow): 
    """
    Classe permettant de créer la fenêtre principale.

    attributs :
        -encMessage : permet de stocker le message lors de l'encodage
        -decMessage : permet de stocker le message lors du decodage
        -encKey : permet de stocker la clé du message crypté lors de l'encodage
        -decKey : permet de stocker la clé du message crypté lors du decondage

    methodes :
        -eraseAll 
        -clickEncryptPageBtn 
    """
    def __init__(self):
        super().__init__()
        uic.loadUi(f"{os.getcwd()}\\front-end\\ui-files\\main.ui", self) # On importe l'interface graphique liée à ce constructeur.

        self.encMessage = ""
        self.decMessage = ""
        self.encKey = ""
        self.decKey = ""

        def eraseAll():
            """
            Méthode qui permet de reinitialiser les valeurs de tous les widgets de l'application.

            C.F. la documentation de PyQt pour connaître l'utilisation de chacune des methodes.
            """
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
            """
            Méthode qui permet d'effectuer l'action d'ouvrir la page de cryptage.
            """
            print("opening 'encrypt page'")
            self.stackedWidget.setCurrentWidget(self.encryptPage)
        def clickDecryptPageBtn():
            """
            Méthode qui permet d'effectuer l'action d'ouvrir la page de décryptage.
            """
            print("opening 'decrypt page'")
            self.stackedWidget.setCurrentWidget(self.decryptPage)
        def clickMenuPageBtn():
            """
            Méthode qui permet d'effectuer l'action d'ouvrir la page de menu.
            """
            print("opening 'menu page'")
            eraseAll()
            self.stackedWidget.setCurrentWidget(self.menuPage)

        def clickEncPswdOkBtn():
            """
            Méthode qui permet de valider le mot de passe dans la page de cryptage.
            """
            print(f"enc key: {self.encPswdLineEdit.text()}")
            self.encKey = self.encPswdLineEdit.text()
            self.runEncBtn.setEnabled(True)
        def clickEncPswdCancelBtn():
            """
            Méthode qui permet de supprimer le texte présent dans la zone de texte de la page de cryptage, consacré au mot de passe.
            """
            self.encPswdLineEdit.clear()
        def clickDecPswdOkBtn():
            """
            Méthode qui permet de valider le mot de passe dans la page de décryptage.
            """
            print(f"dec key: {self.decPswdLineEdit.text()}")
            self.decKey = self.decPswdLineEdit.text()
            self.runDecBtn.setEnabled(True)
        def clickDecPswdCancelBtn():
            """
            Méthode qui permet de supprimer le texte présent dans la zone de texte de la page de décryptage, consacré au mot de passe.
            """
            self.decPswdLineEdit.clear()

        def clickEncMessOkBtn():
            """
            Méthode qui permet de valider le message dans la page de décryptage.
            """
            print(f"message: {self.encMessLineEdit.text()}")
            self.encMessage = self.encMessLineEdit.text()
            self.encPswdLineEdit.setEnabled(True)  
        def clickEncMessCancelBtn():
            """
            Méthode qui permet de supprimer le texte présent dans la zone de texte de la page de décryptage, consacré au message.
            """
            self.encMessLineEdit.clear()

        def encPswdTextChanged():
            """
            Méthode qui permet d'activer ou de désactiver les boutons de dialogue, de la zone de texte consacré au mot de passe dans la zone d'encryptage, selon le contenu de cette dernière.
            """
            if self.encImageLabel.is_imported == True and self.encPswdLineEdit.text() != "":
                self.encPswdBtnBox.setEnabled(True)
            else:
                self.encPswdBtnBox.setEnabled(False)
        def decPswdTextChanged():
            """
            Méthode qui permet d'activer ou de désactiver les boutons de dialogue, de la zone de texte consacré au mot de passe dans la zone de décryptage, selon le contenu de cette dernière.
            """
            if self.decImageLabel.is_imported == True and self.decPswdLineEdit.text() != "":
                self.decPswdBtnBox.setEnabled(True)
            else:
                self.decPswdBtnBox.setEnabled(False)

        def encMessTextChanged():
            """
            Méthode qui permet d'activer ou de désactiver les boutons de dialogue, de la zone de texte consacré au message dans la zone d'encryptage, selon le contenu de cette dernière.
            """
            if self.encImageLabel.is_imported == True and self.encMessLineEdit.text() != "":
                self.encMessBtnBox.setEnabled(True)
            else:
                self.encMessBtnBox.setEnabled(False)

        def clickRunEncBtn():
            """
            Méthode qui permet d"executer l'encryptage du messagee.
            """
            print(f"{self.encMessage}, {self.encKey}, {self.encImageLabel.image_path}")
            encoding_link(path=self.encImageLabel.image_path, message=self.encMessage, key=self.encKey)
            self.encKey = ""
            encDialog = EncryptedDialog()
            encDialog.exec_()

        def clickRunDecBtn():
            """
            Méthode qui permet d"executer le decryptage du messagee.
            """
            self.decMessage = decoding_link(path=self.decImageLabel.image_path, message=False, key=self.decKey)
            print(self.decMessage)
            decDialog = DecryptedDialog()
            decDialog.exec_()


        """
        On relie ici toutes les méthodes avec leur signal respectif.
        """
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
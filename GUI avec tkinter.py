###### GUI avec tkinter  ######

## IMPORT

from tkinter import *
import os
from tkinter import ttk


## PROGRAMME



def unfocus_entrer(event):
    zoneSaisie = entree.get()
    print(zoneSaisie)
    entree.config(state=DISABLED)

def unfocus():
    zoneSaisie = entree.get()
    print(zoneSaisie)
    entree.config(state=DISABLED)

def retry():
    entree.config(state=NORMAL)


def saisie_texte():
    gui = Tk()

    #espace saisie de texte
    cadre = Frame(gui)
    cadre.pack(padx=5, pady=5)
    etiquette = Label(cadre, text='Mot de passe :')
    etiquette.pack(padx=5, pady=5, side=LEFT)
    entree = Entry(cadre, width=50, show="*")
    entree.pack(padx=5, pady=5, side=LEFT)

    #bouton valider
    button = Button(gui, text='valider', command=unfocus)
    button.pack(padx=5,pady=5,side=LEFT)
    gui.bind('<Return>', unfocus_entrer)

    #bouton reesayer
    bouton_retry = Button(gui, text= 'reesayer', command=retry)
    bouton_retry.pack(padx=5,pady=5,side=LEFT)

    gui.mainloop()

##fenetre encodage


##fenetre decodage





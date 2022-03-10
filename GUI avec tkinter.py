###### GUI avec tkinter  ######

## IMPORT

from tkinter import *
import os
from tkinter import ttk


## PROGRAMME

gui = Tk()



cadre = Frame(gui)
cadre.pack(padx=5, pady=5)

etiquette = Label(cadre, text='Mot de passe :')
etiquette.pack(padx=5, pady=5, side=LEFT)

entree = Entry(cadre, width=50, show="*")
entree.pack(padx=5, pady=5, side=LEFT)
entree.focus_force()

zoneSaisie = entree.get()

gui.mainloop()
import tkinter as tk
from PIL import ImageTk, Image
from page import *

width, height = 400,400

screen = tk.Tk()
screen.geometry(f"{screen.winfo_screenwidth()}x{screen.winfo_screenheight()}")

menu = tk.Menu(screen)
menu.add_cascade(label ='Help', menu = tk.Menu())


screen.config(menu=menu)

p1 = Page()
p2 = Page()

image1 = Image.open("../de/chien.png")
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(text="bonjour")
label2 = tk.Label(image=test)

p1.add(label1)
p2.add(label2)

def b1Click():
    p2.hide()
    p1.show()

def b2Click():
    p1.hide()
    p2.show()
                          
button1 = tk.Button(text ="click me", command=b1Click)
button2 = tk.Button(text ="same", command=b2Click)
button1.pack()
button2.pack()

screen.mainloop()
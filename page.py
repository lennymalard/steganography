import tkinter as tk

class Page:
    def __init__(self):
        self.widgets = []
    
    def show(self):
        for w in self.widgets:
            w.pack_forget()
    
    def hide(self):
        for w in self.widgets:
            w.pack()
            
    def add(self, w):
        self.widgets.append(w)
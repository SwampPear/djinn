from tkinter import *
from tkinter import ttk


class Interface:
    def __init__(self):
        self.root = Tk()
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=self.root.destroy).grid(column=1, row=0)


    def run(self):
        self.root.mainloop()

from tkinter import *
from tkinter import ttk


class Style:
    BLACK       = '#0E0E0E'
    DARKGRAY    = '#282828'


class InputBar(ttk.Frame):
    def __init__(self, parent):
        self.parent = parent

        # styling
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('input-bar-container.TFrame', background='#0E0E0E')
        self.style.configure('input-bar.TEntry', fieldbackground='#fcfcfc', relief='flat')

        # container frame (self)
        super().__init__(self.parent, padding=8, style='input-bar-container.TFrame')
        self.grid()
        self.pack(fill=X)

        # input bar
        self.input_bar = ttk.Entry(self, style='input-bar.TEntry')
        self.input_bar.grid(row=0, column=0, sticky=E + W)
        self.grid_columnconfigure(0, weight=1)

        #ttk.Button(self, text="Quit", command=self.parent.destroy).grid(column=0, row=0)


class LogContainer(ttk.Frame):
    def __init__(self, parent):
        self.parent = parent

        # styling
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('log-container.TFrame', background='red')
        self.style.configure('log-message.TText', color='white')

        # container frame (self)
        super().__init__(self.parent, padding=8, style='log-container.TFrame')
        self.grid()


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title('Djinn')
        self.root.geometry('725x450+700+200')
        self.root.configure(bg='#0E0E0E')

        self.log_container = LogContainer(self.root)
        self.input_bar = InputBar(self.root)


    def run(self):
        self.root.mainloop()

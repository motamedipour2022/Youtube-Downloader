from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import re
import threading


class Application:

    def __init__(self, root):
        self.root=root
        self.root.grid_rowconfigure(0,weight=2)
        self.root.grid_columnconfigure
if __name__=="__main__":

    window = Tk()
    window.title("YouTube Download Manager")
    window.state("zoomed")

    app = Application(window)

    mainloop()
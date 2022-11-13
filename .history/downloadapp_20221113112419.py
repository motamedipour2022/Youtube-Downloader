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
        self.root.grid_columnconfigure(0,weight=1)
        self.root.config(bg="#ffdddd")

        top_label = Label(self.root, text="YouTube Downloader", fg="orange", font=('Type Xero',70))
        top_label.grid(pady=(0,20))

        self.youtubeEntryVar = StringVar()

        self.youtubeEntryVar = Entry(self.root)

if __name__=="__main__":

    window = Tk()
    window.title("YouTube Download Manager")
    window.state("zoomed")

    app = Application(window)

    mainloop()
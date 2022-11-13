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
        top_label.grid(pady=(0,10))

        link_label = Label(self.root, text="Please Paste Any YouTube Video Link Below", font=('SnowPersons',30))
        link_label.grid(pady=(0,20))

        self.youtubeEntryVar = StringVar()

        self.youtubeEntryVar = Entry(self.root, width=70, textvariable=self.youtubeEntryVar, font=("Agency Fb", 25), fg="red")
        self.youtubeEntryVar.grid(pady=(0,15),ipady=2)

        self.youtubeEntryError = Label(self.root,text="",font=("Concert one", 20))
        self.youtubeEntryError.grid(pady=(0,8))

        self.youtubeFileSaveLabel = Label(self.root,text="Choose Directory", font=("Concert one", 30))
        self.youtubeFileSaveLabel.grid()

        self.youtubeFileDirectoryButton = Button(self.root,text="Directory", font=("Bell MT", 15),command=self.openDirectory)
        self.youtubeFileDirectoryButton.grid(pady=(10,3))

        self.fileLocationLabel = Label(self.root, text="", font=("Freestyle Script", 25))
        self.fileLocationLabel.grid()

        self.youtubeChoselabel = Label(self.root, text="Chose the Download Type", font=("Variety", 30))
        self.youtubeChoselabel.grid()

        self.downloadChoices = [("Audio Mp3", 1),("Video Mp4", 2)]

        self.ChoicesVar = StringVar()
        self.ChoicesVar.set(1)

        for text,mode in self.downloadChoices:
            self.youtubeChoices = Radiobutton(self.root, text=text, font=("Northwest old", 15), variable=self.ChoicesVar, value=mode)
            self.youtubeChoices.grid()


        self.downloadButton = Button(self.root,text = "Download", width=10, font=("Bell MT", 15),command=checkyoutubelink)
        self.downloadButton.grid(pady=(30,5))

    def checkyoutubelink(self):
        self.matchyoutubelink = re.match("^https://www.youtube.com/.", self.youtubeEntryVar.get())
        if (not self.matchyoutubelink):
            self.youtubeEntryError.config(text="Invalid Youtube Link", fg="red")
        elif (not self.openDirectory()):
            self.fileLocationLabel.config(text="Please Choice a Directory")
        elif(self.matchyoutubelink and self.fileLocationLabel):
            self.downloadWindow()
    def downloadWindow(self):

        self.newWindow = Toplevel(self.root)
        self.root.withdraw()

        self.app = SecondApp(self.newWindow, self.youtubeEntryVar.get(),self.FolderName.get(), self.ChoicesVar.get())





    
    def openDirectory(self):
        self.FolderName=filedialog.askdirectory()

        if(len(self.FolderName)>0):
            self.fileLocationLabel.config(text=self.FolderName, fg="green")
            return True
        else:
            self.fileLocationLabel.config(text="Please Choose a Directory", fg="red")

class SecondApp:
    def __init__(self, downloadWindow, youtubelink, FolderName, Choices):

        self.downloadWindow = downloadWindow
        self.youtubelink = youtubelink
        self.FolderName = FolderName
        self.Choices = Choices

        self.yt = YouTube

if __name__=="__main__":

    window = Tk()
    window.title("YouTube Download Manager")
    window.state("zoomed")

    app = Application(window)

    mainloop()
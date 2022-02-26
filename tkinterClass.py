from tkinter import *
from tkinter import ttk
from scraping import *
from threading import *

class Tkinter:
    def __init__(self):
        self.root = Tk()
        self.root.title(" YT Audio")
    
    def getLink(self):
        link = self.entryLink.get()
        return link

    def frameInput(self):
        frameInput = Frame(self.root)    #ttk.frame(self.root)
        frameInput.pack()

        Label(frameInput, text = "Enter youtube link").grid(row = 0, column = 0)

        self.entryLink = ttk.Entry(frameInput)
        self.entryLink.grid(row = 1, column = 0, ipadx = 300)

        def clickEnter():
            scraping = Scraping()
            thread = Thread(target = scraping.download, args = (self.getLink(),))
            self.entryLink.delete(0, END) 
            thread.start()

        buttonDownload = ttk.Button(frameInput, text = "Enter", command = clickEnter)
        buttonDownload.grid(row = 2, column = 0)

    

    def endProgram(self):
        self.root.mainloop()

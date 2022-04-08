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

    def createOptionMenuType(self):
        self.optionVar = StringVar()
        self.optionVar.set("YT-Audio") 
        optionMenuType = ttk.OptionMenu(self.frameInput, self.optionVar, "YT-Audio", "Podcast", "Music")
        optionMenuType.grid(row = 2, column=0)

    def getOption(self):
        option = self.optionVar.get()
        return option

    def frameInput(self):
        self.frameInput = Frame(self.root)    #ttk.frame(self.root)
        self.frameInput.pack()

        Label(self.frameInput, text = "Enter youtube link").grid(row = 0, column = 0)

        self.entryLink = ttk.Entry(self.frameInput)
        self.entryLink.grid(row = 1, column = 0, ipadx = 300)

        self.createOptionMenuType()

        def clickEnter():
            scraping = Scraping()
            thread = Thread(target = scraping.download, args = (self.getLink(), self.getOption(), self.frameInput,))
            self.entryLink.delete(0, END) 
            thread.start()
            

        buttonDownload = ttk.Button(self.frameInput, text = "Enter", command = clickEnter)
        buttonDownload.grid(row = 3, column = 0)


    

    def endProgram(self):
        self.root.mainloop()

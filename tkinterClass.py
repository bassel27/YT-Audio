from tkinter import *
from tkinter import ttk

from numpy import var
from scraping import *
from threading import *


class Tkinter:
    def __init__(self):
        self.root = Tk()
        self.root.title(" YT Audio")

    def getLink(self):
        link = self.entryLink.get()
        return link

    def createOptionMenuType(frameInput):
        optionVar = StringVar()
        optionVar.set("YT-Audio")
        optionMenuType = ttk.OptionMenu(
            frameInput, optionVar, "YT-Audio", "Podcast", "Music"
        )
        optionMenuType.grid(row=3, column=0)
        return optionVar

    def getOption(optionVar):
        option = optionVar.get()
        return option

    def createCheckButton(self):
        self.checkVar = IntVar()
        self.checkPlaylist = ttk.Checkbutton(
            self.frameInput, text="Playlist?", variable=self.checkVar
        )
        self.checkPlaylist.grid(row=2, column=0)

    def isChecked(self):
        if self.checkVar.get() == 1:
            return 1
        else:
            return 0

    def frameInput(self):
        self.frameInput = Frame(self.root)  # ttk.frame(self.root)
        self.frameInput.pack()

        Label(self.frameInput, text="Enter youtube link").grid(row=0, column=0)

        self.entryLink = ttk.Entry(self.frameInput)
        self.entryLink.grid(row=1, column=0, ipadx=300)

        optionVar = Tkinter.createOptionMenuType(self.frameInput)
        self.createCheckButton()

        def clickEnter():
            scraping = Scraping()
            if self.isChecked() == 1:
                Thread(
                    target=scraping.downloadPlaylistAudio,
                    args=(self.getLink(), optionVar, self.frameInput),
                ).start()
                self.checkVar.set(0)
            else:
                Thread(
                    target=scraping.downloadAudio,
                    args=(
                        self.getLink(),
                        Tkinter.getOption(optionVar),
                        self.frameInput,
                    ),
                ).start()
            self.entryLink.delete(0, END)

        buttonDownload = ttk.Button(self.frameInput, text="Enter", command=clickEnter)
        buttonDownload.grid(row=4, column=0)

    def endProgram(self):
        self.root.mainloop()

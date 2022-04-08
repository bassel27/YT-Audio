from tkinter.tix import COLUMN
from pytube import YouTube
from pytube.cli import on_progress
from tkinter import ttk
from tkinter import *
import os
import arabic_reshaper
from bidi.algorithm import get_display

def formatArabicText(text):
    text = arabic_reshaper.reshape(text)    #reshape text
    return get_display(text)

class Scraping:

    def getFolder(option):
        if option == "YT-Audio":
            folder = '/run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_RZ8NB0PBNWT/Internal storage/Audiobooks/YT-Audio'
        elif option == "Music":
            folder = '/home/basselabdulsabour/Music to Help Study'
        elif option == "Podcast":
            folder = '/run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_RZ8NB0PBNWT/Internal storage/Audiobooks/Podcasts'
        return folder

    def download(self, link, option, frameInput):
        yt = YouTube(link)
        self.title = yt.title
        stream = yt.streams.get_audio_only()
        self.folder = Scraping.getFolder(option)
        self.size = stream.filesize
        try:
            stream.download(self.folder)
        except:
            self.folder = '/home/basselabdulsabour/YT-Audio'
            stream.download()
        self.verifyDownload(frameInput)
        

    def verifyDownload(self, frameInput):
        if '.' in self.title:
            self.title = self.title.replace('.', '')

        try:
            size = os.path.getsize(self.folder + '/' + self.title + '.mp4')
            if(size == self.size):
                Label(frameInput, text =  "✅ " + formatArabicText(self.title)).grid()
        except:
            print(self.title + ": Error")
    
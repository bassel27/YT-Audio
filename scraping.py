from tkinter.tix import COLUMN
from pytube import YouTube
from pytube import Playlist
from tkinter import *
import os
import re
import arabic_reshaper
from bidi.algorithm import get_display

def formatArabicText(text):
    text = arabic_reshaper.reshape(text)    #reshape text
    return get_display(text)

class Scraping:

    def getFolder(option):
        if option == "YT-Audio":
            folder = r"This PC\Bassel's Note\Internal storage\Audiobooks\YT-Audio"
        elif option == "Music":
            folder = r'E:\Music to Help Study'
        elif option == "Podcast":
            folder = r"This PC\Bassel's Note\Internal storage\Audiobooks\Podcasts"
        return folder

    def downloadAudio(self, link, option, frameInput):
        yt = YouTube(link)
        self.title = yt.title
        stream = yt.streams.get_audio_only()
        self.size = stream.filesize
        # self.folder = Scraping.getFolder(option)
        # try:
        #     stream.download(self.folder)
        # except:
        #     self.folder = r'E:\Programming\YT-Audio\tkinterClass.py'
        self.folder = r"E:\Programming\YT-Audio"
        stream.download(self.folder)
        self.verifyDownload(frameInput)
        
    def downloadPlaylistAudio(link):
        playlist = Playlist(link)
        numberVideos = len(playlist.video_urls)
        for video in playlist.videos:
            stream = video.streams.get_audio_only()
            stream.download()

    def verifyDownload(self, frameInput):
        if '.' in self.title:
            self.title = self.title.replace('.', '')

        try:
            size = os.path.getsize(self.folder + '/' + self.title + '.mp4')
            if(size == self.size):
                Label(frameInput, text =  "✅ " + formatArabicText(self.title)).grid()
        except:
            print(self.title + ": Error")

    



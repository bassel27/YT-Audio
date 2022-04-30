from pytube import YouTube
import os
from pytube import Playlist
from tkinter import *
import arabic_reshaper
from bidi.algorithm import get_display
from difflib import SequenceMatcher


def formatArabicText(text):
    text = arabic_reshaper.reshape(text)  # reshape text
    return get_display(text)


class Scraping:
    def getFolder(option):
        if option == "YT-Audio":
            folder = r"This PC\Bassel's Note\Internal storage\Audiobooks\YT-Audio"
        elif option == "Music":
            folder = r"E:\Music to Help Study"
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
        #     self.folder = r'E:\Programming Projects\YT-Audio\tkinterClass.py'
        self.folder = r"E:\Programming Projects\YT-Audio"
        stream.download(self.folder)
        self.verifyDownload(frameInput)

    def downloadPlaylistAudio(self, link, option, frameInput):
        playlist = Playlist(link)
        self.folder = r"E:\Programming Projects\YT-Audio"
        for video in playlist.videos:
            stream = video.streams.get_audio_only()
            stream.download()
            self.title = video.title
            self.size = stream.filesize
            self.verifyDownload(frameInput, True)

    def getSimilarity(self, fileName):
        return SequenceMatcher(isjunk = None, a = self.title, b = fileName).ratio()

    def getDownloadedFileName(self):
        fileNames = os.listdir(r"E:\Programming Projects\YT-Audio") 
        max = 0
        for fileName in fileNames:
            i = self.getSimilarity(fileName)
            if max < i:
                max = i
                title = fileName
        return title

    def verifyDownload(self, frameInput, isPlaylist=False):
        self.title = self.getDownloadedFileName()   # sometimes, the title is not the same as the file name (due to illegal characters), so we need to make the title same as the file name
        try:
            size = os.path.getsize(self.folder + "/" + self.title)
            if size == self.size:
                labelText = "✅ " + formatArabicText(self.title)
                if isPlaylist:
                    labelText += " (playlist)"
                Label(frameInput, text=labelText).grid()
            else:
                Label(frameInput, text=self.title + ": Error").grid()
        except:
            Label(frameInput, text=self.title + ": Error").grid()

from pytube import YouTube
import os
from pytube import Playlist as PL
from tkinter import *
import arabic_reshaper
from bidi.algorithm import get_display
from difflib import SequenceMatcher
from video import Video
from playlist import Playlist

def formatArabicText(text):
    text = arabic_reshaper.reshape(text)  # reshape text
    return get_display(text)


class Scraping(Video):



    def downloadAudio(self, link, option, frameInput):
        yt = YouTube(link)
        stream = yt.streams.get_audio_only()
        self.initializeAttributes(yt.title, link, stream.filesize)
        # self.folder = Scraping.getFolder(option)
        # try:
        #     stream.download(self.folder)
        # except:
        #     self.folder = r'E:\Programming Projects\YT-Audio\tkinterClass.py'
        self.folder = r"E:\Programming Projects\YT-Audio"
        stream.download(self.folder)
        self.verifyDownload(frameInput)

    def downloadPlaylistAudio(self, link, option, frameInput):
        playlist = PL(link)
        self.setPlaylistAttributes(playlist.title, link)
        try:    #make a playlist directory
            os.makedirs("E:\Programming Projects\YT-Audio" + "/" + self.playlistTitle)
        except: 
            pass
        self.folder = "E:\Programming Projects\YT-Audio" + "/" + self.getPlaylistFolderName(self.playlistTitle)
        for video in playlist.videos:
            stream = video.streams.get_audio_only()
            stream.download(self.folder)
            self.title = video.title
            self.size = stream.filesize
            self.verifyDownload(frameInput, True)

    def getSimilarity(self, a, b):
        return SequenceMatcher( None, a , b).ratio()

    def getFileName(self):
        fileNames = fileNames = [os.path.splitext(filename)[0] for filename in os.listdir(self.folder)]
        max = 0
        for fileName in fileNames:
            i = self.getSimilarity(self.title, fileName)
            if max < i:
                max = i
                title = fileName
        return title

    def getPlaylistFolderName(self, playlistTitle):
        fileNames = os.listdir("E:\Programming Projects\YT-Audio") 
        max = 0
        for fileName in fileNames:
            i = self.getSimilarity(playlistTitle, fileName)
            if max < i:
                max = i
                title = fileName
        return title

    def verifyDownload(self, frameInput, isPlaylist=False):
        self.title = self.getFileName()   # sometimes, the title is not the same as the file name (due to illegal characters), so we need to make the title same as the file name
        try:
            size = os.path.getsize(self.folder + "/" + self.title + ".mp4")
            if size == self.size:
                labelText = "✅ " + formatArabicText(self.title)
                if isPlaylist:
                    labelText += " - (playlist: " + self.playlistTitle + ")"
                Label(frameInput, text=labelText).grid()
            else:
                Label(frameInput, text=self.title + ": Error").grid()
        except:
            Label(frameInput, text=self.title + ": Error").grid()



    def setFolder(self, option):
        if option == "YT-Audio":
            self.folder = r"This PC\Bassel's Note\Internal storage\Audiobooks\YT-Audio"
        elif option == "Music":
            self.folder = r"E:\Music to Help Study"
        elif option == "Podcast":
            self.folder = r"This PC\Bassel's Note\Internal storage\Audiobooks\Podcasts"
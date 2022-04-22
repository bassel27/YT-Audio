from tkinter.tix import COLUMN
from pytube import YouTube
from pytube import Playlist
import re
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
            folder = r"This PC\Bassel's Note\Internal storage\Audiobooks\YT-Audio"
        elif option == "Music":
            folder = r'E:\Music to Help Study'
        elif option == "Podcast":
            folder = r"This PC\Bassel's Note\Internal storage\Audiobooks\Podcasts"
        return folder

    def download(self, link, option, frameInput):
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
        

    def verifyDownload(self, frameInput):
        if '.' in self.title:
            self.title = self.title.replace('.', '')

        try:
            size = os.path.getsize(self.folder + '/' + self.title + '.mp4')
            if(size == self.size):
                Label(frameInput, text =  "✅ " + formatArabicText(self.title)).grid()
        except:
            print(self.title + ": Error")







# YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
# DOWNLOAD_DIR = r"E:\Programming\YT-Audio"
# playlist = Playlist('https://www.youtube.com/playlist?list=PLzwWSJNcZTMSW-v1x6MhHFKkwrGaEgQ-L')

# # this fixes the empty playlist.videos list
# playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

# # physically downloading the audio track
# for video in playlist.videos:
#     audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
#     audioStream.download(output_path=DOWNLOAD_DIR)
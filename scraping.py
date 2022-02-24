from asyncio import streams
from pytube import YouTube
from pytube.cli import on_progress

class Scraping:
    
    def download(self, link):
        yt = YouTube(link, on_progress_callback=on_progress)
        stream = yt.streams.get_audio_only()
        stream.download()
        self.tilte = yt.title
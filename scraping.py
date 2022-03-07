from pytube import YouTube
from pytube.cli import on_progress

class Scraping:
    
    def download(self, link):
        yt = YouTube(link)
        stream = yt.streams.get_audio_only()
        try:
            stream.download('/run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_RZ8NB0PBNWT/Internal storage/Audiobooks/YT-Audio')
        except:
            stream.download()

        self.tilte = yt.title
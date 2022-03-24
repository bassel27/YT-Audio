from pytube import YouTube
from pytube.cli import on_progress

class Scraping:

    def getFolder(option):
        if option == "YT-Audio":
            folder = '/run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_RZ8NB0PBNWT/Internal storage/Audiobooks/YT-Audio'
        elif option == "Music":
            folder = '/home/basselabdulsabour/Music to Help Study'
        elif option == "Podcast":
            folder = '/run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_RZ8NB0PBNWT/Internal storage/Audiobooks/Podcasts'
        return folder

    def download(self, link, option):
        yt = YouTube(link)
        self.title = yt.title
        stream = yt.streams.get_audio_only()
        try:
            stream.download(Scraping.getFolder(option))

        except:
            stream.download()

    
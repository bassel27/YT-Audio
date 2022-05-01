from playlist import Playlist


class Video(Playlist):
    def initializeAttributes(self, title, link, size):
        self.title = title
        self.link = link
        self.size = size    
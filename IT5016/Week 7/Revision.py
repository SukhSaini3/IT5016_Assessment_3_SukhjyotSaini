class Album:
    def __init__(self,name,artist,year):
        self.name = name
        self.artist = artist
        self.year = year

    def album_release(self):
        print(f"The album titled {self.name} by {self.artist} was released in {self.year}")

album1 = Album("Harry Styles", "Fine Line", 2019)
album1.album_release()

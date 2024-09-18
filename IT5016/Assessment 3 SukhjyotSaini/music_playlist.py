"""
Question: Python program to create a music library system using OOP.
Author: Sukhjyot Singh Saini
"""

class Song():
    def __init__(self, title, artist, genre, duration):
        self.title = title #An instance of the Title class
        self.artist = artist  # An instance of the Artist class
        self.genre = genre #An instance of the Genre class
        self.duration = duration  # Duration in seconds

    def format_duration(self):
        minutes, seconds = divmod(self.duration, 60)
        return f"{minutes}m {seconds}s"

    def __str__(self):
        return f"{self.title} by {self.artist.name} [{self.genre}] - {self.format_duration()}"

    
class Artist():
    def __init__(self, name):
        self.name = name
        self.songs = []  # List to store songs by this artist

    def add_song(self, song):
        self.songs.append(song) #Appennd function adds new values to the list

    def __str__(self):
        return self.name

    
class MusicLibrary():
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        song.artist.add_song(song)  # Add the song to the artist's song list

    def list_songs(self):
        if self.songs:
            print("Available Songs:")
            for song in self.songs:
                print(song)
        else:
            print("No Songs Available")

    def find_song(self, title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                return song
        return None

    
def menu():
    print("Music Library System Menu:")
    print("1. List Available Songs")
    print("2. Add a Song to the Library")
    print("3. Find a Song by Title")
    print("4. Exit")


def main():
    library = MusicLibrary()

    # Create artists
    artist1 = Artist("The Beatles")
    artist2 = Artist("Adele")

    # Create songs
    library.add_song(Song("Hey Jude", artist1, "Rock", 431))
    library.add_song(Song("Someone Like You", artist2, "Pop", 285))
    library.add_song(Song("Let It Be", artist1, "Rock", 243))

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.list_songs()

        elif choice == "2":
            title = input("Enter Song Title: ").strip()
            artist_name = input("Enter Artist Name: ").strip()
            genre = input("Enter Song Genre: ").strip()
            duration = int(input("Enter Song Duration (in seconds): ").strip())
            artist = Artist(artist_name)
            library.add_song(Song(title, artist, genre, duration))
            print(f"Song '{title}' added to the library.")

        elif choice == "3":
            title = input("Enter Song Title to Find: ").strip()
            song = library.find_song(title)
            if song:
                print(f"Found: {song}")
            else:
                print("Song not found.")

        elif choice == "4":
            print("Exiting...")
            break #Exits the program

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

********** Music Library System **********
Author: Sukhjyot Singh Saini

Overview:

The Music Library System is a simple console application developed in Python that allows users to manage a collection of songs. It utilizes object-oriented programming (OOP) principles to create a structured and maintainable codebase. This application supports adding songs, listing all available songs, and searching for songs by title.

Features:

Add Songs: Easily add new songs to the library.
List Songs: Display all songs in the library with their details.
Find Songs: Search for a song by title.
Artist Management: Each song is associated with an artist, allowing for organized management of songs.
Design Principles

KISS (Keep It Simple, Stupid)
The code is structured to be straightforward and easy to understand. Each class has a clear responsibility:

Song: Represents a song and its properties.
Artist: Represents an artist and manages their songs.
MusicLibrary: Manages the collection of songs and provides methods for interacting with them.

DRY (Don't Repeat Yourself)
The program avoids code duplication by encapsulating functionalities within classes and methods. For example:

The add_song method in the MusicLibrary class handles both adding the song to the library and associating it with the artist.
The song formatting and display logic is contained within the Song class, ensuring that the display logic is centralized.
OOP (Object-Oriented Programming)
The system uses OOP principles to enhance code organization and reusability:

Encapsulation: Song and Artist details are encapsulated within their respective classes.
Abstraction: Users interact with high-level methods without needing to understand the underlying implementation details.

Requirements:

Python 3.x installed on your machine.

User Instructions: 

Upon starting the application, a menu will be displayed.
Choose an option by entering the corresponding number:
1: List Available Songs
2: Add a Song to the Library
3: Find a Song by Title
4: Exit
Follow the prompts to add songs or search for them.

Future Enhancements:

Implement persistent storage (e.g., saving to a file or database) to maintain songs across sessions.
Add features for editing or deleting songs.
Create a user interface (UI) for a more user-friendly experience.


License:

This project is open-source and available under the MIT License.
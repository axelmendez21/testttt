# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 6 Assignment 3

def make_album(artist, album_title, numsongs = 'None'):
    album = {'artist': artist,
             'title': album_title,
             'number of songs': numsongs}
    return album

while True:
    title = input("What is the title of the album (or q for quit)? ")
    if title == 'q':
        break
    artist = input("What is the name of the artist? ")
    print(make_album(title,artist))


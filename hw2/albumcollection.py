"""
Name: Ou Liu
Date: 2021-10-27
Brief Class Description:
This class should contain a single attribute: a list of Album objects, and the following methods:
o __init__
o __str__
o load albums (from csv file into Album objects in the list)
o save albums (from album list into csv file)
o add album – add a single Album object to the albums attribute
o sort (by the key passed in, then by year) (attrgetter from [2])
"""

import csv
from album import Album


class AlbumCollection:
    def __init__(self):
        """
        constructor
        """
        self.albums = []

    def __str__(self):
        """
        string to be printed
        """
        result = ''
        for album in self.albums:
            result += str(album) + '\n'
        return result

    def load_albums(self, filename):
        """
        load albums (from csv file into Album objects in the list)
        :param filename: file name
        """
        with open(filename, "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                title = row[0]
                artist = row[1]
                year = int(row[2])
                is_completed = row[3]
                if (is_completed == 'r'):
                    self.albums.append(Album(title, artist, year, False))
                else:
                    self.albums.append(Album(title, artist, year, True))

    def save(self, file):
        """
        save albums (from album list into csv file)
        :param filename: file name
        """
        with open(file, 'w') as f:
            for album in self.albums:
                if (album.is_completed):
                    f.write('{},{},{},c\n'.format(album.title, album.artist, album.year))
                else:
                    f.write('{},{},{},r\n'.format(album.title, album.artist, album.year))

    def add_album(self, album):
        """
        add a single Album object to the albums attribute
        :param album: album object to be added
        """
        self.albums.append(album)

    def sort(self, key='artist'):
        """
        sort (by the key passed in, then by year)
        :param key: sort key
        """
        if (key == 'title'):
            self.albums = sorted(self.albums, key=lambda x: (x.title, x.year))
        elif (key == 'artist'):
            self.albums = sorted(self.albums, key=lambda x: (x.artist, x.year))
        elif (key == 'year'):
            self.albums = sorted(self.albums, key=lambda x: x.year)
        elif (key == 'is_completed'):
            self.albums = sorted(self.albums, key=lambda x: (x.is_completed, x.year))
    def get_unvisited_num(self):
        return 1

    def get_album_by_title(self, title):
        """
        get the album by title
        :return: title
        """
        for album in self.albums:
            if album.title == title:
                return album


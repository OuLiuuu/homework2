"""
Name: Ou Liu
Date: 2021-10-27
Brief Class Description:
This should be a simple class with the required attributes for an album
(title, artist, year and a Boolean for whether it is completed) and the methods:
o __init__
o __str__
o mark_required
o mark_completed
"""


class Album:
    def __init__(self, title='', artist='', year=0, is_completed=False):
        """
        constructor
        :param title: title, str
        :param artist: artist, str
        :param year: year, int
        :param is_completed: is_completed, boolean
        """
        self.title = title
        self.artist = artist
        self.year = year
        self.is_completed = is_completed

    def __str__(self):
        """
        string to be printed
        :return: s
        """
        if self.is_completed:
            return "{} by {},({})(completed)".format(self.title, self.artist, self.year)
        return "{} by {},({})".format(self.title, self.artist, self.year)

    def mark_required(self):
        """
        mark the album as required
        """
        self.is_completed = False

    def mark_completed(self):
        """
        mark the album as completed
        """
        self.is_completed = True

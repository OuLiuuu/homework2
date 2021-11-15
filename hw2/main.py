"""
Name: Ou Liu
Date: 2021-10-27
Brief Project Description:
"""
# Create your main program in this file, using the AlbumTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from albumcollection import AlbumCollection
from album import Album

class AlbumTrackerApp(App):
    def __init__(self, **kwargs):
        """
        Install all the widgets in kivy app
        """
        self.FILENAME = 'albums.csv'
        #  You might like to consider using a dictionary to help with mapping the GUI text to the attributes of the class to be sorted by.
        self.text2attr = {'Artist': 'artist', 'Title': 'title' , 'Year': 'year', 'Completed': 'is_completed'}
        super().__init__(**kwargs)
        # The data (model) for this program should be a single AlbumCollection object.
        self.album_collection = AlbumCollection()
        # Sorting by the label
        self.sort_by_label = Label(text="Sort by:")
        # sort by the is_visited attribution default
        # The left side of the screen contains a drop-down "spinner" for the user to choose the sorting
        self.spinner = Spinner(text='Artist', values=('Artist', 'Title', 'Year', 'Completed'))
        self.add_new_album_label = Label(text="Add New Album...")
        self.title_label = Label(text="Title:")
        self.title_text_input = TextInput(write_tab=False, multiline=False)
        self.artist_label = Label(text="Artist:")
        self.artist_text_input = TextInput(write_tab=False, multiline=False)
        self.year_label = Label(text="Year:")
        self.year_text_input = TextInput(write_tab=False, multiline=False)

        # Add Album and clear labels
        self.add_album_button = Button(text='Add Album')
        self.clear_button = Button(text='Clear')


    def build(self):
        """
        Open the kivy app and implement all widgets
        """
        # The program should load the CSV file of albums using the method from AlbumCollection.
        self.root = Builder.load_file('app.kv')
        self.album_collection.load_albums(self.FILENAME)
        self.album_collection.sort()
        self.left_panel_widgets()
        self.right_panel_widgets()
        self.root.ids.bottom_panel.text = 'Welcome to Album Tracker 2.0.'
        return self.root

    def left_panel_widgets(self):
        """
        Build left panel and add widgets to it
        """
        # left
        self.root.ids.left_panel.add_widget(self.sort_by_label)
        self.root.ids.left_panel.add_widget(self.spinner)
        self.root.ids.left_panel.add_widget(self.add_new_album_label)
        self.root.ids.left_panel.add_widget(self.title_label)
        self.root.ids.left_panel.add_widget(self.title_text_input)
        self.root.ids.left_panel.add_widget(self.artist_label)
        self.root.ids.left_panel.add_widget(self.artist_text_input)
        self.root.ids.left_panel.add_widget(self.year_label)
        self.root.ids.left_panel.add_widget(self.year_text_input)
        self.root.ids.left_panel.add_widget(self.add_album_button)
        self.root.ids.left_panel.add_widget(self.clear_button)
        # bind sort function
        self.spinner.bind(text=self.sort_album)
        # bind add album error check function
        self.add_album_button.bind(on_release=self.error_checker)
        # bind clear_text function
        self.clear_button.bind(on_release=self.clear_text)

    def right_panel_widgets(self):
        """
        Build right panel and add widgets to it
        """
        # right widgets
        # add all albums to the right panel
        for album in self.album_collection.albums:
            # The right side contains a button for each album, colour-coded based on whether the album
            #  is completed or not (the actual colour scheme is up to you).
            if album.is_completed:
                album_item = Button(text=str(album))
                album_item.id = album.title
                album_item.background_color = [41, 36, 33, 0.3]
            else:
                album_item = Button(text=str(album))
                album_item.id = album.title
                album_item.background_color = [0, 201, 87, 0.6]
            # bind album click event
            # When the user clicks on a album button, the album changes between completed and required
            album_item.bind(on_release=self.album_click)
            self.root.ids.right_panel.add_widget(album_item)

    def sort_album(self, *args):
        """
        Sort the albums according to the user's choice
        """
        #
        self.album_collection.sort(self.text2attr[self.spinner.text])
        self.root.ids.right_panel.clear_widgets()
        self.right_panel_widgets()

    def album_click(self, button):
        """
        Organize the status of the selected album
        :param button: button to be clicked
        """
        # When the user clicks on an album button, the album changes between completed and required
        # The text to display when an album button is clicked is like below
        # complete the album
        if not self.album_collection.get_album_by_title(button.id).is_completed:
            self.album_collection.get_album_by_title(button.id).is_completed = True
            # You completed title.
            self.root.ids.bottom_panel.text = "You completed {}.".format(
                self.album_collection.get_album_by_title(button.id).title)
        # require the album
        else:
            self.album_collection.get_album_by_title(button.id).is_completed = False
            # # You need to listen to title.
            self.root.ids.bottom_panel.text = "You need to listen to {}.".format(
                self.album_collection.get_album_by_title(button.id).title)
        # update the right_panel
        self.sort_album()
        self.root.ids.right_panel.clear_widgets()
        self.right_panel_widgets()

    def clear_text(self, *args):
        """
        Clear all text fields
        """
        # Whenever the user clicks the “Clear” button, all text in the input fields and the status
        # label should be cleared.
        self.title_text_input.text = ""
        self.artist_text_input.text = ""
        self.year_text_input.text = ""
        self.root.ids.bottom_panel.text = ""

    def error_checker(self, *args):
        """
        To check if the input is valid or not
        """
        # The user can add a new album by entering text in the input fields and clicking “Add Album”.
        # no empty input
        # All album fields are required. If a field is left blank, the bottom status label should display
        #  “All fields must be completed” when “Add Album” is clicked.
        if self.title_text_input.text == '' \
                or self.artist_text_input.text == '' \
                or self.year_text_input.text == '':
            self.root.ids.bottom_panel.text = "All fields must be completed"
        else:
            try:
                year = int(self.year_text_input.text)
                # year > 0
                if year <= 0:
                    # If year is <= 0, the status label should display “Year must be > 0”.
                    self.root.ids.bottom_panel.text = "Year must be > 0"
                # correct input
                else:
                    self.album_collection.add_album(Album(self.title_text_input.text,
                                                        self.artist_text_input.text,
                                                        year))
                    self.album_collection.sort(self.text2attr[self.spinner.text])
                    # When the user successfully adds an album, the entry fields should be cleared and the
                    # new album button should appear on the right. You can clear and then re-create the
                    # button objects to do this. (dynamic_widgets from [3])
                    self.clear_text()
                    self.root.ids.right_panel.clear_widgets()
                    self.right_panel_widgets()
            # year input must be a number
            # The status bar at the bottom shows program messages.
            except ValueError:
                # The year field must be a valid integer. If this is invalid (and no other fields
                #  are empty), the status bar should display “Please enter a valid number”.
                self.root.ids.bottom_panel.text = "Please enter a valid number"

    def stop(self):
        """
        The albums file must be saved (there's a method for that!) when the program ends,
        updating any changes made with the app by the user
        """
        # The albums file must be saved when the program ends, updating any changes made
        # with the app by the user (use on_stop method from [4]).
        self.album_collection.save(self.FILENAME)


if __name__ == '__main__':
    AlbumTrackerApp().run()

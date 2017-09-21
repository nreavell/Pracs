

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

__author__ = 'Nathan Reavell'


class DynamicWidgetsApp(App):
    """ Main program - Kivy app to demo dynamic widget creation """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        self.name_list = ["john", "dave", "greg"]

    def build(self):
        self.title = "name loop"
        self.root = Builder.load_file('name_loop.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        for name in self.name_list:
            # create a button for each phonebook entry
            temp_button = Label(text=name)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_button)

DynamicWidgetsApp().run()

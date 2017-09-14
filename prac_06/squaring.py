from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Nathan Reavell'

class SquareNumberApp(App):
    """Kivy App for squaring a number."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (400, 150)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call),
        output result to label widget."""
        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()

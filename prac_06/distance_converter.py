from kivy.app import App
from kivy.lang import Builder


miles_to_km = 1.609


class MilesConverterApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('distance_converter.kv')
        return self.root

    def handle_convert(self):
        value = self.get_valid_miles()
        result = value * miles_to_km
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_convert()

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

MilesConverterApp().run()
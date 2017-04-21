from kivy.app import App
from kivy.lang import Builder


class MilesToKilometres(App):
    def build(self):
        self.title = "Miles To Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_increment(self, value):
        try:
            self.root.ids.input_number.text = str(int(self.root.ids.input_number.text) + value)
        except ValueError:
            self.root.ids.input_number.text = str(value)

    def handle_convert(self, value):
        try:
            self.root.ids.output_box.text = str(int(value) * 1.60934)
        except ValueError:
            self.root.ids.output_box.text = "0.0"

MilesToKilometres().run()

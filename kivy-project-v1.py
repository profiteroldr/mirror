from kivy.app import App
from kivy.uix.label import Label

class Program(App):
    def build(self):
        self.title = "Yazbel"

        return Label(text = "Merhaba Dünya")

Program().run()
from kivy.app import App
from kivy.uix.label import Label # Ekranda yazı göstermeyi sağlar.
from kivy.uix.boxlayout import BoxLayout # Butonlar oluşturmayı sağlar.

class Program(App):
    def build(self):
        duzen = BoxLayout()

        yazi1 = Label(text = "Merhaba")

        yazi2 = Label(text = "Dünya")

        duzen.add_widget(yazi1)
        duzen.add_widget(yazi2)

        return duzen

Program().run()
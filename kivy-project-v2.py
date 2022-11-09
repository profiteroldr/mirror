from kivy.app import App
from kivy.uix.label import Label # Ekranda yazı göstermeyi sağlar.

class Program(App):
    def on_start(self):
        self.title = "Yazbel"
        # bir takım işlemler...

    def on_stop(self):
        # Uygulama kapatılırken...
        pass

    def on_pause(self):
        # Uygulama arkaplana alınırken...
        # Burda return True yapmanız gerekiyor
        return True

    def on_resume(self):
        # Tekrar giriş yapıldığında yazımızı değiştiriyoruz
        self.yazi.text = "Programa tekrar hoşgeldiniz"

    def build(self):
        self.yazi = Label(text = "Merhaba Dünya")
        return self.yazi

Program().run()
from kivy.app import App
from kivy.uix.label import Label # Ekranda yazı göstermeyi sağlar.
from kivy.uix.floatlayout import FloatLayout  # Pencere düzeni sağlanmasını sağlar.

# gerekli sınıfları import ettik

class Program(App):
    def build(self):

        duzen = FloatLayout() # pencere düzenimizi tanımladık

        buton = Label(text = "Merhaba",
                                size_hint = (.1,.1),
                                pos = (10,10))

        duzen.add_widget(buton) # butonumuzu yerleştiriyoruz

        return duzen


Program().run()
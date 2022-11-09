from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Program(App):
    def build(self):

        self.anaDuzen = BoxLayout() # Elemanların hepsini tutan ana pencere düzenimiz

        self.ilkSatir = BoxLayout()
        self.ikinciSatir = BoxLayout()

        self.hava = Label(text = "Hava Durumu")

        self.saat = Label(text = "Saat")

        self.ilkSatir.add_widget(self.hava)

        self.ikinciSatir.add_widget(self.saat)

        # Şimdi hepsini ana düzene yerleştiriyoruz

        self.anaDuzen.add_widget(self.ilkSatir)
        self.anaDuzen.add_widget(self.ikinciSatir)

        return self.anaDuzen

    def kontrol(self,event = None):
        if(self.nickKutu.text == "admin" and self.sifreKutu.text == "12345"):
            print("Giriş Basarili")

        else:
            print("Hatalı Giris")


Program().run()
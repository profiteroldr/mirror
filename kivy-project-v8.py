from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Program(App):
    def build(self):

        # Ana BOX
        self.anaDuzen = BoxLayout() # Elemanların hepsini tutan ana pencere düzenimiz

        # Alt BOX
        self.ilkSatir = BoxLayout() # BoxLayout olarak tanımladık.
        self.ikinciSatir = BoxLayout()

        # İçerikler/Widget Oluşturma (BOXların içine gelecek içerikler/widgetler.)
        self.hava = Label(text = "Hava Durumu")
        self.saat = Label(text = "Saat")

        # Widget Tanımlama (Oluşturulan widgetleri Alt BOXlara tanımlıyoruz.)
        self.ilkSatir.add_widget(self.hava)
        self.ikinciSatir.add_widget(self.saat)

        # Şimdi hepsini ana düzene yerleştiriyoruz
        # Ana BOXa yerleştirme. (Widgetleri Alt BOXlara yerleştirdikten sonra, Alt BOXları Ana BOXa yerleştiriyoruz.)
        self.anaDuzen.add_widget(self.ilkSatir)
        self.anaDuzen.add_widget(self.ikinciSatir)

        # Ana BOXumuzu return ile geri döndürerek ekrana ekranda gösterilmesini sağlıyoruz.
        return self.anaDuzen

Program().run()
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import datetime
import locale
from kivy.clock import Clock
from kivy.uix.image import Image
import requests
from googletrans import Translator # pip install googletrans==4.0.0-rc1 ile sorunu çözdüm.



class Program(App):
    def build(self):

        # Ana BOX
        self.anaDuzen = BoxLayout() # Elemanların hepsini tutan ana pencere düzenimiz

        # Alt BOX
        # BoxLayout olarak tanımladık.
        self.ilkSatir = BoxLayout(orientation = "vertical") # ilkSatir içindeki widgetleri alt alta yerleştirdik.
        self.ikinciSatir = BoxLayout() # ikinciSatir ile ilkSatir default yani varsayılan olarak yan yana dizilecektir. Fakat ilkSatir içindeki widgetler bu durumdan etkilenmeyecek ve alt alta yerleştirilecektir.

        Clock.schedule_interval(self.saat_hesaplama,0) # 1 saniye sonra, self.saat_hesaplama adlı fonksiyonu çalıştır
        Clock.schedule_interval(self.hava_durumu,0) # 1 saniye sonra, self.saat_hesaplama adlı fonksiyonu çalıştır

        a = 1
        while a == 1:
            self.havadurumu = input("Hava durumunu giriniz: ")
            
            if self.havadurumu == "gunesli":
                self.havadurumu = "D:/Python Projeler/Kivy\kivy-gorseller/gunesli-gorsel.png"
                a = 0
            elif self.havadurumu == "yagmurlu":
                self.havadurumu = "D:/Python Projeler/Kivy\kivy-gorseller/yagmurlu-gorsel.png"
                a = 0
            elif self.havadurumu == "bulutlu":
                self.havadurumu = "D:/Python Projeler/Kivy\kivy-gorseller/bulutlu-gorsel.png"
                a = 0
            elif self.havadurumu == "firtinali":
                self.havadurumu = "D:/Python Projeler/Kivy\kivy-gorseller/firtinali-gorsel.png"
                a = 0
            elif self.havadurumu == "aksam":
                self.havadurumu = "D:/Python Projeler/Kivy\kivy-gorseller/aksam-acik-hava-gorsel.png"
                a = 0
 
        # İçerikler/Widget Oluşturma (BOXların içine gelecek içerikler/widgetler.)
        self.hava = Image(source = "{}".format(self.havadurumu)) #hava görselini tanmladık
        self.time = Label(markup = True)
        self.derece = Label(markup = True)

        # Widget Tanımlama (Oluşturulan widgetleri Alt BOXlara tanımlıyoruz.)
        self.ilkSatir.add_widget(self.hava)
        self.ikinciSatir.add_widget(self.time)
        self.ilkSatir.add_widget(self.derece)

        # Şimdi hepsini ana düzene yerleştiriyoruz
        # Ana BOXa yerleştirme. (Widgetleri Alt BOXlara yerleştirdikten sonra, Alt BOXları Ana BOXa yerleştiriyoruz.)
        self.anaDuzen.add_widget(self.ilkSatir)
        self.anaDuzen.add_widget(self.ikinciSatir)

        # Ana BOXumuzu return ile geri döndürerek ekrana ekranda gösterilmesini sağlıyoruz.
        return self.anaDuzen
    
    # Saat Hesaplaması Yapılan Yer
    def saat_hesaplama(self,event):
        zaman = datetime.datetime.now()
        self.saat = "[size=90sp]{}:{}:{}[/size]".format(zaman.hour,zaman.minute,zaman.second)
        self.time.text = self.saat
    
    # Hava Durumu Hesaplaması Yapılan Yer
    def hava_durumu(self,event):
        self.sehir_ismi = "Istanbul"
        
        api = "89f43f1f20b6e6c6e3a602d47906405b"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        url = base_url + "appid=" + api + "&q=" + self.sehir_ismi

        gelen_veri = requests.get(url)
        gelen_veri_json = gelen_veri.json()

        if (gelen_veri_json["cod"] != "404"):

            temp = gelen_veri_json["main"]["temp"]
            description = gelen_veri_json["weather"][0]["description"]
            pressure = gelen_veri_json["main"]["pressure"]
            country = gelen_veri_json["sys"]["country"]

            self.sicaklik = str(int(temp) - 273)
            self.havaDurumu = str(description)
            self.basinc = str(pressure)
            self.lokasyon = self.sehir_ismi + " " + str(country)
            
            translator = Translator()
            sentence = self.havaDurumu
            example = translator.translate(sentence,dest="tr")
            example = example.text
            example = example.title()
            self.havaDurumu = example


            self.derece.text = """[size=50sp]
            {}°C
            Hava Durumu: {} 
            Lokasyon: {}[/size]""".format(self.sicaklik,self.havaDurumu,self.lokasyon)

        else:
            print("Böyle bir şehir bulunamadı!")


Program().run()



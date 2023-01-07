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
from kivy.core.window import Window
import os

# Çeviri API'si arzalı olduğu için çeviri otomatik olarak yapılıyor.

class Program(App):
    def build(self):
        
        ################################################################################################################################
        self.sehir_ismi = "Ankara"
        
        api = "89f43f1f20b6e6c6e3a602d47906405b"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        url = base_url + "appid=" + api + "&q=" + self.sehir_ismi

        self.gelen_veri = requests.get(url)
        self.gelen_veri_json = self.gelen_veri.json()
        self.description = self.gelen_veri_json["weather"][0]["description"]
        self.hava_durumu_gorsel = str(self.description)

        # https://www.flaticon.com/packs/weather-432?word=weather
        # https://www.flaticon.com/packs/weather-162?word=weather
        # https://www.flaticon.com/packs/weather-120?word=weather

        a = 1
        while a == 1:
            self.hava_durumu_gorsel = self.hava_durumu_gorsel # Hava durumu için hangi görsellerin kullanılacağı belirlendiği yer. Hava Durumu Görsel Belirleme Referans Adresi: https://openweathermap.org/weather-conditions
        
            if self.hava_durumu_gorsel == "clear sky":
                self.hava_durumu_gorsel = "D:/Python Projeler/Kivy/kivy-gorseller/acikhava.png"
                a = 0
            elif self.hava_durumu_gorsel == "few clouds":
                self.hava_durumu_gorsel = "D:/Python Projeler/Kivy/kivy-gorseller/azbulutlu-gunduz.png"
                a = 0
            elif self.hava_durumu_gorsel == "scattered clouds":
                self.hava_durumu_gorsel = "D:/Python Projeler/Kivy/kivy-gorseller/parcalibulutlu.png"
                a = 0
            elif self.hava_durumu_gorsel == "broken clouds":
                self.hava_durumu_gorsel = "D:/Python Projeler/Kivy/kivy-gorseller/yeryerbulutlu.png"
                a = 0
            elif self.hava_durumu_gorsel == "shower rain":
                self.hava_durumu_gorsel = "D:/Python Projeler/Kivy/kivy-gorseller/yagisli.png"
                a = 0 
            elif self.hava_durumu_gorsel == "rain":
                self.hava_durumu_gorsel = "D:/Python Projeler/Kivy/kivy-gorseller/sagnakyagisli.png"
                a = 0
            elif self.hava_durumu_gorsel == "thunderstorm":
                self.hava_durumu_gorsel = "D:/Python Projeler/Kivy/kivy-gorseller/gokgurultulufırtına.png"
                a = 0 
            elif self.hava_durumu_gorsel == "snow":
                self.hava_durumu_gorsel = "D:/Python Projeler/Kivy/kivy-gorseller/karyagisli.png"
                a = 0
            elif self.hava_durumu_gorsel == "mist":
                self.hava_durumu_gorsel = "D:/Python Projeler/Kivy/kivy-gorseller/sisli.png"
                a = 0
        ################################################################################################################################

        # Ana BOX
        self.anaDuzen = BoxLayout() # Elemanların hepsini tutan ana pencere düzenimiz

        # Alt BOX
        # BoxLayout olarak tanımladık.
        self.ilkSatir = BoxLayout(orientation = "vertical") # ilkSatir içindeki widgetleri alt alta yerleştirdik.
        self.ikinciSatir = BoxLayout() # ikinciSatir ile ilkSatir default yani varsayılan olarak yan yana dizilecektir. Fakat ilkSatir içindeki widgetler bu durumdan etkilenmeyecek ve alt alta yerleştirilecektir.

        Clock.schedule_interval(self.saat_hesaplama,0) # 0 saniye sonra, self.saat_hesaplama adlı fonksiyonu çalışır.
        Clock.schedule_interval(self.hava_durumu_hesaplama,0) # 0 saniye sonra, self.hava_durumu_hesaplama adlı fonksiyonu çalışır.

        # İçerikler/Widget Oluşturma (BOXların içine gelecek içerikler/widgetler.)
        self.hava = Image(source = "{}".format(self.hava_durumu_gorsel)) #hava görselini tanmladık
        self.veri = Label(markup = True)
        self.time = Label(markup = True)

        # Widget Tanımlama (Oluşturulan widgetleri Alt BOXlara tanımlıyoruz.)
        self.ilkSatir.add_widget(self.hava)
        self.ilkSatir.add_widget(self.veri)
        self.ikinciSatir.add_widget(self.time)
        
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
    
    # Hava durumu hesaplaması yapılan ve ekrana bastırılacak verilerin ayarlandığı yer.
    def hava_durumu_hesaplama(self,event):

        if (self.gelen_veri_json["cod"] != "404"):

            temp = self.gelen_veri_json["main"]["temp"]
            description = self.gelen_veri_json["weather"][0]["description"]
            pressure = self.gelen_veri_json["main"]["pressure"]
            country = self.gelen_veri_json["sys"]["country"]

            self.sicaklik = str(int(temp) - 273)
            self.hava_durumu_bilgisi = str(description)
            self.basinc = str(pressure)
            self.lokasyon = self.sehir_ismi + " " + str(country) 

            # Çeviri API'si arzalı olduğu için çeviri otomatik olarak yapılıyor.
            if self.hava_durumu_bilgisi == "clear sky":
                self.hava_durumu_bilgisi = "Açık Hava"

            elif self.hava_durumu_bilgisi == "few clouds":
                self.hava_durumu_bilgisi =  "Az Bulutlu"

            elif self.hava_durumu_bilgisi == "scattered clouds":
                self.hava_durumu_bilgisi = "Parçalı Bulutlu"

            elif self.hava_durumu_bilgisi == "broken clouds":
                self.hava_durumu_bilgisi = "Yer Yer Bulutlu"

            elif self.hava_durumu_bilgisi == "shower rain":
                self.hava_durumu_bilgisi = "Sağnak Yağışlı"

            elif self.hava_durumu_bilgisi == "rain":
                self.hava_durumu_bilgisi = "Yağmurlu"

            elif self.hava_durumu_bilgisi == "thunderstorm":
                self.hava_durumu_bilgisi = "Gökgürültülü Yağışlı"

            elif self.hava_durumu_bilgisi == "snow":
                self.hava_durumu_bilgisi = "Kar Yağışlı"

            elif self.hava_durumu_bilgisi == "mist":
                self.hava_durumu_bilgisi = "Sisli"
            
            else:
                self.hava_durumu_bilgisi = "Lütfen Sistem Yönetisi İle İletişime Geçiniz."


            self.veri.text = """[size=50sp]
            {}°C
            Hava Durumu: {} 
            Lokasyon: {}[/size]""".format(self.sicaklik,self.hava_durumu_bilgisi,self.lokasyon)

        else:
            print("Böyle bir şehir bulunamadı!")

Window.maximize() # Otomatik geniş ekran ile başlatıyor uygulamayı.
#os.startfile("personal-asistant-v25.py") # Bu kod ile sesli asistan program ile birlikte otomatik çalışıyor. Fakat bu programında aynı dosya yolunda olması gerekmektedir.

Program().run()


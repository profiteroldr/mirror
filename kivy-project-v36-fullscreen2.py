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
from kivy.core.window import Window




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

        ###############################

        self.sehir_ismi = "Ankara"
        
        api = "89f43f1f20b6e6c6e3a602d47906405b"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        url = base_url + "appid=" + api + "&q=" + self.sehir_ismi

        self.gelen_veri = requests.get(url)
        self.gelen_veri_json = self.gelen_veri.json()
        self.description = self.gelen_veri_json["weather"][0]["description"]

        self.havaDrm = str(self.description)
            
        translator = Translator()
        sentence = self.havaDrm
        example = translator.translate(sentence,dest="tr")
        example = example.text
        example = example.title()
        self.havaDrm = example

        ################################
        # https://www.flaticon.com/packs/weather-432?word=weather
        # https://www.flaticon.com/packs/weather-162?word=weather
        # https://www.flaticon.com/packs/weather-120?word=weather
        a = 1
        while a == 1:
            self.havadurumu = self.havaDrm # Hava durumu için hangi görsellerin kullanılacağı belirlendiği yer. Hava Durumu Görsel Belirleme Referans Adresi: https://openweathermap.org/weather-conditions
        
            if self.havadurumu == "Açık Hava":
                self.havadurumu = "D:/Python Projeler/Kivy/kivy-gorseller/acikhava.png"
                a = 0
            elif self.havadurumu == "Bulutlar":
                self.havadurumu = "D:/Python Projeler/Kivy/kivy-gorseller/azbulutlu-gunduz.png"
                a = 0
            elif self.havadurumu == "Dağınık Bulutlar":
                self.havadurumu = "D:/Python Projeler/Kivy/kivy-gorseller/parcalibulutlu.png"
                a = 0
            elif self.havadurumu == "Kırık Bulutlar":
                self.havadurumu = "D:/Python Projeler/Kivy/kivy-gorseller/yeryerbulutlu.png"
                a = 0
            elif self.havadurumu == "Duş Yağmuru":
                self.havadurumue = "D:/Python Projeler/Kivy/kivy-gorseller/yagisli.png"
                a = 0 
            elif self.havadurumu == "Yağmur":
                self.havadurumu = "D:/Python Projeler/Kivy/kivy-gorseller/sagnakyagisli.png"
                a = 0
            elif self.havadurumu == "Fırtına":
                self.havadurumu = "D:/Python Projeler/Kivy/kivy-gorseller/gokgurultulufırtına.png"
                a = 0 
            elif self.havadurumu == "Kar":
                self.havadurumu = "D:/Python Projeler/Kivy/kivy-gorseller/karyagisli.png"
                a = 0
            elif self.havadurumu == "Sis":
                self.havadurumu = "D:/Python Projeler/Kivy/kivy-gorseller/sisli.png"
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

        if (self.gelen_veri_json["cod"] != "404"):

            temp = self.gelen_veri_json["main"]["temp"]
            description = self.gelen_veri_json["weather"][0]["description"]
            pressure = self.gelen_veri_json["main"]["pressure"]
            country = self.gelen_veri_json["sys"]["country"]

            self.sicaklik = str(int(temp) - 273)
            self.havaDrm = str(description)
            self.basinc = str(pressure)
            self.lokasyon = self.sehir_ismi + " " + str(country)
            
            translator = Translator()
            sentence = self.havaDrm
            example = translator.translate(sentence,dest="tr")
            example = example.text
            example = example.title()
            self.havaDrm = example

            if self.havaDrm == "Açık Hava":
                self.havaDrm = "Açık Hava"

            elif self.havaDrm == "Bulutlar":
                self.havaDrm = "Az Bulutlu"

            elif self.havaDrm == "Dağınık Bulutlar":
                self.havaDrm = "Parçalı Bulutlu"

            elif self.havaDrm == "Kırık Bulutlar":
                self.havaDrm = "Yer Yer Bulutlu"

            elif self.havaDrm == "Duş Yağmuru":
                self.havaDrm = "Yağışlı"

            elif self.havaDrm == "Yağmur":
                self.havaDrm = "Sağnak Yağışlı"

            elif self.havaDrm == "Fırtına":
                self.havaDrm = "Gökgürültülü Yağışlı"
            
            elif self.havaDrm == "Kar":
                self.havaDrm = "Kar Yağışlı Yağışlı"

            elif self.havaDrm == "Sis":
                self.havaDrm = "Sisli"

        

            self.derece.text = """[size=50sp]
            {}°C
            Hava Durumu: {} 
            Lokasyon: {}[/size]""".format(self.sicaklik,self.havaDrm,self.lokasyon)

        else:
            print("Böyle bir şehir bulunamadı!")

Window.fullscreen = 'auto' # Otomatik tam ekran (fullscreen) ile başlatıyor uygulamayı.

Program().run()


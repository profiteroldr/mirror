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

import hava_durumu_sorgulama
import gorsel_sistemi
import saat_sistemi

gorsel_sistemi.hava_durumu_bilgisi = str(gorsel_sistemi.hava_durumu_bilgisi)


class Program(App):
    def build(self):


        # Ana BOX
        self.anaDuzen = BoxLayout() # Elemanların hepsini tutan ana pencere düzenimiz

        # Alt BOX
        # BoxLayout olarak tanımladık.
        self.ilkSatir = BoxLayout(orientation = "vertical") # ilkSatir içindeki widgetleri alt alta yerleştirdik.
        self.ikinciSatir = BoxLayout() # ikinciSatir ile ilkSatir default yani varsayılan olarak yan yana dizilecektir. Fakat ilkSatir içindeki widgetler bu durumdan etkilenmeyecek ve alt alta yerleştirilecektir.

        Clock.schedule_interval(self.saat_fonk,0) # 0 saniye sonra, self.saat_hesaplama adlı fonksiyonu çalışır.

        # İçerikler/Widget Oluşturma (BOXların içine gelecek içerikler/widgetler.)
        self.hava = Image(source = "{}".format(gorsel_sistemi.hava_durumu_bilgisi)) #hava durumu için görsel tanımlama işlemini yaptık
        self.veri = Label(markup=True, text=hava_durumu_sorgulama.deneme, font_size=50)
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
    def saat_fonk(self,event):
        saat_sistemi.saat_hesaplama()
        self.time.text = saat_sistemi.saat_hesaplama()

Window.maximize() # Otomatik geniş ekran ile başlatıyor uygulamayı.
#Window.fullscreen = 'auto' # Otomatik tam ekran (fullscreen) ile başlatıyor uygulamayı.

#os.startfile("personal-asistant-v25.py") # Bu kod ile sesli asistan program ile birlikte otomatik çalışıyor. Fakat bu programında aynı dosya yolunda olması gerekmektedir.

Program().run()


import requests
import threading
import time
import api_sistemi

url = api_sistemi.url
sehir_ismi = "Ankara"

def api_sorgu_sistemi():

     #API den sorgu yapıyoruz.
    api_sorgu = requests.get(url)

     #API den gelen verileri JSON formatına dönüştürüyoruz ve bunu api_json_cevirme parametresine atıyoruz.
    api_json_cevirme = api_sorgu.json()

    #JSON formatına dönüştürülen verilerin ismini daha düzgün hale getirmemiz lazım. Şimdi ise yeniden isimlendiriyoruz.
    json_veri = api_json_cevirme

    if (json_veri["cod"] != "404"):

        #json_veri içerisinden istediğimiz verileri çekiyoruz.
        sicaklik = json_veri["main"]["temp"]
        hava_durumu_bilgisi = json_veri["weather"][0]["description"]
        basinc = json_veri["main"]["pressure"]
        ulke = json_veri["sys"]["country"]

        #Çektiğimiz verileri düzenliyor ve yine kendi isimleri ile kendilerine atıyoruz.
        sicaklik = str(int(sicaklik) - 273)
        hava_durumu_bilgisi = str(hava_durumu_bilgisi)
        basinc = str(basinc)
        lokasyon = sehir_ismi + " " + str(ulke) 


        #JSON dan gelen veriler İngilizce olduğu için Türkçe'ye çeviriyoruz. En son olarak retrun ile elde edilen çeviriyi geriye döndürüyoruz.
        if hava_durumu_bilgisi == "clear sky":
            hava_durumu_bilgisi = "Açık Hava"
        
        elif hava_durumu_bilgisi == "light rain":
            hava_durumu_bilgisi = "Yağmurlu"
         

        elif hava_durumu_bilgisi == "few clouds":
            hava_durumu_bilgisi =  "Az Bulutlu"
            

        elif hava_durumu_bilgisi == "scattered clouds":
            hava_durumu_bilgisi = "Parçalı Bulutlu"
            

        elif hava_durumu_bilgisi == "broken clouds":
            hava_durumu_bilgisi = "Yer Yer Bulutlu"
            

        elif hava_durumu_bilgisi == "shower rain":
            hava_durumu_bilgisi = "Sağnak Yağışlı"
            

        elif hava_durumu_bilgisi == "rain":
            hava_durumu_bilgisi = "Yağmurlu"
            

        elif hava_durumu_bilgisi == "thunderstorm":
            hava_durumu_bilgisi = "Gökgürültülü Yağışlı"
            

        elif hava_durumu_bilgisi == "snow":
            hava_durumu_bilgisi = "Kar Yağışlı"
            

        elif hava_durumu_bilgisi == "mist":
            hava_durumu_bilgisi = "Sisli"


        #Çeviri sisteminde bir arza olduğu zaman aşağıda bulunan else kısmı devreye girecek.
        else:
            hava_durumu_bilgisi = "Lütfen, sistem yöneticisi ile iletişime geçiniz. Hata: {}".format(hava_durumu_bilgisi)
            

    #404 hatası alındığında yani sistemde bir arza olduğu zaman aşağıda bulunan else kısmı devreye girecek.
    else:
        print("Böyle bir şehir bulunamadı!")

    #Şimdi elde edilen verileri ve yapılan Tr-Eng çevirilerini toplu bir şekilde bir başka parametreye atayalım.
    veri = """
    {}°C
    Hava Durumu: {}
    Lokasyon: {}""".format(sicaklik,hava_durumu_bilgisi,lokasyon)
        
    return veri, hava_durumu_bilgisi


sonuc = api_sorgu_sistemi()

#print(sonuc[0])
#print(sonuc[1])


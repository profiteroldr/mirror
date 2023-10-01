import hava_durumu_sorgulama

#print(hava_durumu_sorgulama.sonuc)
#print(hava_durumu_sorgulama.sonuc[1])

hava_durumu_bilgisi = hava_durumu_sorgulama.sonuc[1]

a = 1
while a == 1:
    if hava_durumu_bilgisi == "Açık Hava":
        hava_durumu_bilgisi = "C:/Projeler/PythonProjeler/KivyProject/kivy-gorseller/acikhava.png"
        a = 0
    elif hava_durumu_bilgisi == "Az Bulutlu":
        hava_durumu_bilgisi = "C:/Projeler/PythonProjeler/KivyProject/kivy-gorseller/azbulutlu-gunduz.png"
        a = 0
    elif hava_durumu_bilgisi == "Parçalı Bulutlu":
        hava_durumu_bilgisi = "C:/Projeler/PythonProjeler/KivyProject/kivy-gorseller/parcalibulutlu.png"
        a = 0
    elif hava_durumu_bilgisi == "Yer Yer Bulutlu":
        hava_durumu_bilgisi = "C:/Projeler/PythonProjeler/KivyProject/kivy-gorseller/yeryerbulutlu.png"
        a = 0
    elif hava_durumu_bilgisi == "Sağnak Yağışlı":
        hava_durumu_bilgisi = "C:/Projeler/PythonProjeler/KivyProject/kivy-gorseller/yagisli.png"
        a = 0 
    elif hava_durumu_bilgisi == "Yağmurlu":
        hava_durumu_bilgisi = "C:/Projeler/PythonProjeler/KivyProject/kivy-gorseller/sagnakyagisli.png"
        a = 0
    elif hava_durumu_bilgisi == "Gökgürültülü Yağışlı":
        hava_durumu_bilgisi = "C:/Projeler/PythonProjeler/KivyProject/kivy-gorseller/gokgurultulufırtına.png"
        a = 0 
    elif hava_durumu_bilgisi == "Kar Yağışlı":
        hava_durumu_bilgisi = "C:/Projeler/PythonProjeler/KivyProject/kivy-gorseller/karyagisli.png"
        a = 0
    elif hava_durumu_bilgisi == "Sisli":
        hava_durumu_bilgisi = "C:/Projeler/PythonProjeler/KivyProject/kivy-gorseller/sisli.png"
        a = 0
    else:
        hava_durumu_bilgisi = "C:/Projeler/PythonProjeler/KivyProject/kivy-gorseller/hata.png" # Hata durumlarında verilecek görsel eklendi.
        a = 0

import datetime

def saat_hesaplama():
        zaman = datetime.datetime.now()
        saat = "[size=90sp]{}:{}:{}[/size]".format(zaman.hour,zaman.minute,zaman.second)
        return saat

saat_hesaplama()

#print(type(saat_hesaplama)) #<class 'function'>
#print(type(saat_hesaplama())) #<class 'str'> #fonksiyonun ismini öğrenmiş oluruz


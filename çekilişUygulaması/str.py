import random
import time



kulanicilar=list()
def kullanici_ekle(x):
      print("-"*30)
      print("Kulanıcı Ekleme Ekranına Hoşgeldiniz")
      ekle=input("Lütfen eklenecek  kullanıcıyı yazınız :")
      kulanicilar.append(ekle)
      input("Devam Etmek için Enter Tuşuna Basınız...")
def kullanici_gor(x):
      say=1
      print("-"*30)
      for i in x:
            print(str(say)+"-Kullanıcı Adı :",i)
            say+=1
      print("-"*30)
      input("Devam Etmek için Enter Tuşuna Basınız...")
def sec(x):
    print("-"*30)
    say=1
    kisi_sec=int(input("Kaç kişi seçilsin? :"))
    rastgele_sec=random.sample(x,kisi_sec)
    print("-"*30)
    for i in rastgele_sec:
      print(str(say)+"-Kullanıcı Adi:",i)
      say+=1
      print("Diger kişi sistemden çekiliyor...")
      time.sleep(3)
    print("-"*30)
    input("Devam Etmek için Enter Tuşuna Basınız...")

def salla(x):
     say=1
     random.shuffle(x)
     print("-"*30)
     for i in x:
           print(str(say)+"-Kullanıcı Adi:",i)
           say+=1
     print("-"*30)
     input("Devam Etmek için Enter Tuşuna Basınız...")
while True:
     print("******ÇEKLİŞ UYGULAMASINA HOŞGELDİNİZ******")
     secim=int(input("1-Kullanıcı Ekle\n2-Kullanıcı Gör\n3-Kullanıcıları Karıştır\n4-Rastgele Seç\n"))
     if secim==1:
          kullanici_ekle(kulanicilar)
     elif secim== 2:
          kullanici_gor(kulanicilar)
     elif secim==3:
          salla(kulanicilar)
     elif secim==4:
          sec(kulanicilar)
     else:
          print("lütfen uygun bir tercih yapınız")
      
          


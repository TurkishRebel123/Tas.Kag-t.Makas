import random
d1 = ["tas","kagit","makas"]
while(1):
 deger =(input)("Taş kağıt makas değerlerinden birini giriniz; ")
 deger = deger.lower()
 deger = deger.replace("ş","s")
 deger = deger.replace("ı","i")
 deger = deger.replace("ğ","g")
 d2 = random.choice(d1)

 print("Bilgisayar "+d2+" seçti" )
 if (d2==deger ):
      print("Berabere!")
      print("Devam etmek için Enter'a basınız")
      a = input("Oyundan çıkmak için E harfine basınız: ")
      if (a == "e"):
       break
 if (d2 == "tas"):
    if (deger == "kagit"):
        print("Kazandin!")
    elif (deger == "makas"):
        print("Kaybettin!")
    else:
        print("Yanlış giriş yaptınız")
 elif (d2 == "makas"):
    if (deger == "tas"):
        print("Kazandin!")
    elif (deger == "kagit"):
        print("Kaybettin!")
    else:
        print("Yanlış giriş yaptınız")
 elif (d2 == "kagit"):
    if (deger == "tas"):
        print("Kaybettin!")
    elif (deger == "makas"):
        print("Kazandın!")
    else:
        print("Yanlış giriş yaptınız")
 print("Devam etmek için Enter'a basınız: ")
 a = input("Oyundan çıkmak için E harfine basınız: ")
 a = a.lower()
 if (a=="e"):
  break



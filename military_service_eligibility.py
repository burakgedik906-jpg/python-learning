okula_gidiyor=input("Okuma durumunuzu belirtiniz? (evet:e, hayir:h)")
yas=int(input("Yas giriniz"))
if yas>=18 and okula_gidiyor=="h":
    print("Askere gelme yasiniz geldi!")
elif yas>=18 and okula_gidiyor=="e":
    print("Okulunuz bittiginde askere gideceksiniz!")
else:
    print("Askerlik yasiniz daha gelmedi")

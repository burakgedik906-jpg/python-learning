vize_notu=int(input("Vize notu giriniz "))
final_notu=int(input("Final notu giriniz "))
ortalama=(vize_notu*0.40) + (final_notu*0.60)
print("Ortalamaniz: ", ortalama)
if ortalama>=50:
    print("Geçti")
else:
    print("Kaldi")

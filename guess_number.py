import random

secret_number=random.randint(1,100) 
guess=0
atttemps=0 

print("1 ile 100 arasinda bir sayi tuttum") 
while guess!=secret_number:
  guess=int(input("tahminin")) 
  attemps+=1

if guess<secret_number:
  print("daha buyuk bir sayi dene") 
elif guess>secret_number:
  print("daha buyuk bir sayi dene") 
else:
  print(f"tebrikler! {attemps} denemede bildin") 
  

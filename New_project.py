#print("Tere tulemast!") #вывод на экран
#nimi=input("введите имя:") #ввод
#print()
#print(f"{nimi}, sul on väga ilus nimi!")
#print(nimi, ", sul on väga ilus nimi") #->tühik
#print(nimi+", sul on väga ilus nimi") # str+str
#vanus=int(input("Kui vana sa oled?"))
#print(nimi, "sa oled"+str(vanus)+"aastat vana")
#vanus+=10

from math import *
print("Võrdse pindalaga ristkülik ja ring")
a=float(input("Anna laius: "))
b=float(input("Anna kõkgus: "))
S=a*b #-;+;*;/;**;//;%
P=a*2+b*2
d=round(sqrt(a**2+b**2),2)
RR=round(sqrt(S/pi), 2)
print(f"Pandala = {S}\nLäbimõtt = {P}\nDiagonaal = {d}\nRingi radius = {RR}")
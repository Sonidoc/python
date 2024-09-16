import os
from random import randint

os.system('cls')

radie = float (input("Vad är det du vill räkna ut:"))
print("svar:" , radie ** 2 * 3.14 )




baldur_online = True
height = 0
weight = 0

while True:

    name = input("Vad mitt namn är? Jag glum.")
    if not name.isnumeric(): 
        break
    else:
        print("skriv bokstäver")


print(name +"," + " Just det, det är mitt namn ")

while True:
    
    name = input("Vad DITT namn är? ")
    if not name.isnumeric(): 
        break
    else:
        print("Skriv ditt jävla namn")

print("Välkommen!" + name)


while True:

    name = (input("Hur gammal du är?"))
    if not name.isalpha():
        break
    else:
        print("du är inte så där mycket gammal")
          
print(name + "!?"+ " Du e dinosaurie. ")


dice = int(input("hur många tärningar? "))

rolls = dice

while True:
    die = randint(1, 6)
    print(die)
    rolls -= 1
    if rolls == 0:
        break



while True:
    try: 
        weight = float(input("Välkommen till BMI-Kalkylator, vänligen ange din vikt i Kg:"))
        break
    except:
        print("Skriv din vikt")
        continue

while True:
    try:
        height = float(input("Ange din längd i meter snälla. T.ex 1.52:")) 
        break
    except:
        print("Fuck gör du, skriv din längd i meter")
        continue
        
print(weight / height**2)  
        


###ujinwegeg


if baldur_online:
    while True:
        try:
            height = float (input("Höjd: "))
            break
        except:
            print("Skriv höjd i nummer")
        continue
    if height >= 1.4 and height <= 1.99:
        print("Du får åka") 

    else:
        print("Du får inte åka")  

else:
    print("baldur är tyvärr stängd")



#ioigjewigwiojgwijgepri

radie = input("Vad är det du vill räkna ut:")
print("svar:" , radie**2 *3.14 )










    

 
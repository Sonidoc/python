

#MODul2 - VARIABLER


#DATATPYER I PYTHON
"""
sträng, string = "text"
heltal,integer = 1... 2... 3... 10
flyttal, float =1.2 skriv alltid flyttal med punk som decimal

boolesk, boo lean = true/false falgga eller av och på


deklarera / initiera

let value; #deklarera

"""
#initera (namn på variabel samt datatyp)
name= "" #string
value= 1.3 #float
value2 = 8 #integer
value3 = 8.1 #float
check = False #boolean
import os



weight = float(input("Välkommen till BMI-Kalkylator, vänligen ange din vikt i Kg:"))


height = float(input("Ange din längd i meter snälla. T.ex 1.52:")) 

print(weight / height**2)  


weight = float(input("Jag undrar hur mycket du väger i lbs, Vänligen ange din vikt i kg här:"))

print(weight * 2.2)





x = input("x: ") #input är sträng från början - du måste typkonvertera innan du gör beräkningar
y = input("y: ")

print("svar:", int(x) * int (y))

# upphöjt görs med **
# modulo görs med % och visar på resten

name = input("Vad mitt namn är? Jag glum.")

print(name +"," + " Just det, det är mitt namn ")

name = input("Vad du heta?:")

print("Välkommen!" + name)

name = input("Hur gammal du är?")

print(name + "!?"+ " Du e dinosaurie. ")

print("Livet i veckor. Mitt namn är Pablo och dagen denna inlämning ska in så är jag sjuk och får inte höra vad min lärare sa idag. Jag vet ingenting om vad jag ska ens göra. Jag har sökt på internet och kollat saker min lärare Johan har skickat men jag hittar ändå ingenting. Jag kommer ihåg att han nämnde att man inte får göra sena inlämningar så jag kan inte vänta en dag till, det här är inte mitt fel.")

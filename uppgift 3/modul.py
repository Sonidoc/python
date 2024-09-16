import os
from random import randint
os.system('cls')

#villkor = if-satser användas för att kontrollera olika utfall i ett program 
#användning:

# = betyder att du tilldelar värde true
# == betyder att man jamför t.ex True

fire_alarm = True
fire_extinguisher = True

if fire_alarm: 
    print("ALARM!")
    #fler funktioner och delar av programmet kan köras här
else:
    print("Allt är frid och fröjd skolan äröppen")

#MNKEy
print(randint(1,6)) #random integer heltal

while True:
    random_number = randint(1,6)
    print(random_number)
    
    if random_number == 6:
        break




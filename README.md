# Zahlenraten
In "Zahlenraten" kann man wie es schon der Name sagt, zahlen raten. 
[Zahlenraten.py](https://github.com/user-attachments/files/26157381/Zahlenraten.py)
# Code
```
import random
import time


def Zahlenraten():
    größe_random = int(input(f"wähle ein Zahl von 1 bis:"))
    bestimmte_zahl = random.randint(1,(größe_random)) 
    time.sleep(.1)
    print("Zahl wird Zufällig gewählt..")
    time.sleep(1)
    deine_zahl = int(input(f"Rate welche zahl es ist:"))
    time.sleep(1)
    
    if deine_zahl > bestimmte_zahl:
        print("Deine zahl ist Leider Größer, richtige zahl wäre gewesen:",(bestimmte_zahl))
    if deine_zahl < bestimmte_zahl:
        print("Deine zahl ist Leider Kleiner, richtige zahl wäre gewesen:",(bestimmte_zahl))
    if bestimmte_zahl == deine_zahl:
        print("Deine zahl ist Richtig! die gesuchte Zahl war:",(bestimmte_zahl))
    

loop = 0

print("(--Zahlen raten--)")
print("danke das du dieses Programm benutzt :)")


while loop == 0:
    Zahlenraten()
    time.sleep(2)

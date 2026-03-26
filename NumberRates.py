import random
import time


def Number_Rates():
    size_random = int(input(f"choose a number from 1 to:"))
    specific_number = random.randint(1,(size_random)) 
    time.sleep(.1)
    print("Number is chosen randomly..")
    time.sleep(1)
    your_number = int(input(f"Guess what number it is:"))
    time.sleep(1)
    
    if your_number > specific_number:
        print("Unfortunately your number is larger, the correct number would have been:",(specific_number))
    if your_number < specific_number:
        print("Unfortunately your number is smaller, the correct number would have been:",(specific_number))
    if specific_number == your_number:
        print("Your number is correct! was the number we were looking for:",(specific_number))
    

loop = 0

print("(--Number Rates--)")
print("thank you for using this program :)")


while loop == 0:
    Number_Rates()
    time.sleep(2)

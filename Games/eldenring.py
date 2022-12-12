from random import randint
from time import sleep
def eldenring():
    # First beast battle
    beast = randint(0, 1)
    tarnished = input("Your first beast approaches. Prepare to battle. Pick 0 or 1(0/1): ")
    if beast == tarnished:
        print("Beast VANQUISHED!! Congrats fellow player.")
    else:
        print("You died.")
        exit()
    sleep(2)

    # Margit
    tarnished = input("Boss battle. Get scared. It's Margit. Pick a number between 0-5(0/1/2/3/4/5): ")
    beast = randint(0, 5)
    if beast == tarnished or tarnished == "pls help me":
        print("Beast VANQUISHED!! Congrats fellow player.")
    else:
        print("You died.")
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a random number between 1 and {x}: "))
        if guess < random_number:
            print("Guessed Number is too low. Try Again!")
        elif guess > random_number:
            print(" Guessed Number too high! Try Again!")
    print("Congrats!")
guess(10)

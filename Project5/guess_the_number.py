import random

def comp_guess(x):
    a = random.randint(1,x)
    guess = 0
    while guess != a:
        guess = int(input(f"Guess the Number, between 1 and {x}: "))
        if guess < a:
            print("Sorry, too low!")
        elif guess > a:
            print("Sorry, too high!")
    print(f"Congrats you guessed the right number {a}")

def user_guess(z,x):
    a = int(input("Number: "))
    guess = random.randint(z,x)
    y = 1
    while guess != a:
        y += 1
        if guess < a:
            print(f"Computer Guess: {guess}")
            print("Sorry, too low!.")
            z = guess+1
            guess = random.randint(z,x)
        elif guess > a:
            print(f"Computer Guess: {guess}")
            print("Sorry, too high!")
            x = guess - 1
            guess = random.randint(z,x)
    print(f"Congrats, computer gussed your number in {y} times")


user_guess(1,100)
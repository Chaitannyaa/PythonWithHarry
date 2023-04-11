import random

r = random.randint(1, 100)
guess = 0
a = None
while guess>=0:
    try:
        a = (input("Please enter your guess number or 'q' to quit: "))
        if a == 'q':
            print("Thank you for playing this game!")
            break   
        a=int(a)
        guess += 1
        if r == a:
            print(f"You guessed it right in trying {guess} guesses")
            break
        elif r > a:
            print("Please enter larger number!")
        elif r < a:
            print("Please enter smaller number!")
    except ValueError:
        print("Please enter an integer")

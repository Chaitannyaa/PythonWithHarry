import random

randomNo = random.randint(1, 100)

guessNo = None
guess = 0

while randomNo != guessNo:
    guessNo = int(input("Enter your Guess : "))
    guess += 1
    if randomNo == guessNo:
        print(f"You Guessed it Right in {guess} Guesses !")
    else:
        if randomNo<guessNo:
            print("You Guessed it Wrong ! Enter the smaller number")
        else:
            print("You Guessed it Wrong ! Enter the larger number")
    

with open("hiscore.txt", 'r') as f:
    hiscore = int(f.read())
print(f"The hiscore was {hiscore}")

if hiscore>guess:
    print("You have just broken the high score!")
    with open("hiscore.txt", 'w') as f:
        f.write(str(guess))
    
with open("hiscore.txt", 'r') as f:
    hiscore = int(f.read())
print(f"New hiscore you set is {hiscore}")

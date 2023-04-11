# Rock Paper and Scissors
import random

def GameWin(Comp, You):
    if Comp == You:
        return None

    elif Comp == 'Rock':
        if You == 'Paper':
            return True
        elif You == 'Scissor':
            return False
    
    elif Comp == 'Paper':
        if You == 'Rock':
            return False
        elif You == 'Scissor':
            return True    
    
    elif Comp == 'Scissor':
        if You == 'Rock':
            return True
        elif You == 'Paper':
            return False    

print("Computer's Turn : Rock{r}, Paper{p} or Scissor{s} ?")

RandNo=random.randint(1,3)
if RandNo == 1:
    Comp = 'Rock'
elif RandNo == 2:
    Comp = 'Paper'
elif RandNo == 3:
    Comp = 'Scissor'

You = input("Your Turn : Rock{r}, Paper{p} or Scissor{s} ?  ")
You=You.lower()
if You == 'r':
    You = 'Rock'
elif You == 'p':
    You = 'Paper'
elif You == 's':
    You = 'Scissor'

print(f"Computer Chose :  {Comp}")
print(f"You Chose :  {You}")

a = GameWin(Comp, You)

if a==None:
    print("Game is Tie!")
elif a:
    print("You Won!")
else:
    print("Computer Won!")
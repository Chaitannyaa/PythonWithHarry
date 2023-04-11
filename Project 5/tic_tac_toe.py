def sum(a,b,c):
    return a+b+c

def displayboard(xTurn, oTurn):
    zero= 'X' if xTurn[0] else 'O' if oTurn[0] else '0'
    one= 'X' if xTurn[1] else 'O' if oTurn[1] else '1'
    two= 'X' if xTurn[2] else 'O' if oTurn[2] else '2'
    three= 'X' if xTurn[3] else 'O' if oTurn[3] else '3'
    four= 'X' if xTurn[4] else 'O' if oTurn[4] else '4'
    five= 'X' if xTurn[5] else 'O' if oTurn[5] else '5'
    six= 'X' if xTurn[6] else 'O' if oTurn[6] else '6'
    seven= 'X' if xTurn[7] else 'O' if oTurn[7] else '7'
    eight= 'X' if xTurn[8] else 'O' if oTurn[8] else '8'
    
    print("/-----------\\")
    print(f"| {zero} | {one} | {two} |")
    print("|---|---|---|")
    print(f"| {three} | {four} | {five} |")
    print("|---|---|---|")
    print(f"| {six} | {seven} | {eight} |")
    print("\-----------/")

def gameWin(xTurn, oTurn):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(xTurn[win[0]],xTurn[win[1]],xTurn[win[2]]) == 3):
            print(" X Won the match")
            from emoji import emojize
            print(emojize(":thumbs_up:"))
            return 1
        if (sum(oTurn[win[0]],oTurn[win[1]],oTurn[win[2]]) == 3):
            print(" O Won the match")
            from emoji import emojize
            print(emojize(":thumbs_up:"))
            return 0
    return -1

xTurn=[0,0,0,0,0,0,0,0,0]
oTurn=[0,0,0,0,0,0,0,0,0]
choice = [0,1,2,3,4,5,6,7,8]
turn = 1
print("Welcome to Tic-Tac-Toe Game")
displayboard(xTurn, oTurn)
while choice:
    if turn == 1:
        print("X's Turn:")
        value = int(input("Enter the value: "))
        if value in choice:
            choice.remove(value)
            xTurn[value] = 1
        else:
            print("You are not allowed to overwrite\n Please other Choice ?")
            turn = 1 - turn

    else:
        print("O's Turn:")
        value = int(input("Enter the value: "))
        if value in choice:
            choice.remove(value)
            oTurn[value] = 1
        else:
            print("You are not allowed to overwrite\n Please other Choice ?")
            turn = 1 - turn

    displayboard(xTurn, oTurn)
    Checking = gameWin(xTurn, oTurn)
    if Checking != -1:
        print("Match Over")
        break
    turn = 1 - turn
print("Match is Tie !")
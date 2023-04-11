# def game():
#     return 1

# score = game()
# with open("hiscore.txt") as f:
#     hiScoreStr = f.read()
    
# if hiScoreStr=='':
#     with open("hiscore.txt", "w") as f:
#         f.write(str(score))

# elif int(hiScoreStr)<score :
#     with open("hiscore.txt", "w") as f:
#         f.write(str(score))


def game():
    a = input("Enter the number of your choice: ")
    return int(a)


Score = game()

with open('newScore.txt', 'r') as f:
    hiScoreStr = f.read()

if hiScoreStr == '':
    with open('newScore.txt', 'w') as f:
        f.write(Score)
if int(hiScoreStr) < Score:
    with open('newScore.txt', 'w') as f:
        f.write(str(Score))

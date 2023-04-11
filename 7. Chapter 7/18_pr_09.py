# n = 3
# for i in range(3):
#     print("*", end="")
#     if i == (n-i-1):
#         print(" ", end="")
#     else:
#         print("*", end="")
#     print("*")

# n = 3
# for i in range(3):
#     print("*", end="")
#     if i == (n-i-1):
#         print(" ", end="")
#     else:
#         print("*", end="")
#     print("*")


#           ****
#           *  *
#           *  *
#           ****


n = 4
for i in range(4):
    print("*", end="")
    if i == (n-i) or i == (n-i-2):
        print(" ", end="")
    else:
        print("*", end="")
    if i == (n-i) or i == (n-i-2):
        print(" ", end="")
    else:
        print("*", end="")
    print("*")

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# num4 = int(input("Enter number 4: "))

# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4

# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3

# if(f1>f2):
#     print(str(f1) + " is greatest") # This f1 is used str to avoid error
# else:
#     print(str(f2) + " is greatest")


# n1 = int(input("Enter number 1: "))
# n2 = int(input("Enter number 2: "))
# n3 = int(input("Enter number 3: "))
# n4 = int(input("Enter number 4: "))

# if (n1>n2):
#     if (n1>n3):
#         if(n1>n4):
#             print("n1 is greatest")
# elif (n2>n3):
#     if(n2>n4):
#         print("n2 is greatest")
# elif (n3>n4):
#     print("n3 is greatest")
# else:
#     print("n4 is greatest")

from functools import reduce
List = []
for i in range(1, 5):
    a = int(input(f"Enter the number {i} : "))
    List.append(a)
print(reduce(max, List))
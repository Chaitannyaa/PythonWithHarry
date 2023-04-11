# num = int(input("Enter the number: "))
# for i in range(0,10):
#     n=10-i
#     print(f"{num} X {n} = {num*n}")


n = int(input("Enter the number: "))
print(f"Multiplication table of {n} in reversed order is :")

for i in range(0,10):
    j = 10 - i
    print(f"{n} X {j} = {n*j}")
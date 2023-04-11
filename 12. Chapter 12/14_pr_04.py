# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))

# try:
#     print(a/b)
# except:
#     print("Infinite")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

try:
    print(a/b)
except ZeroDivisionError:
    print("Infinite")
# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

# def sum(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     return n + sum(n-1)

# n=int(input("Enter the value of n: "))
# s=sum(n)
# print(f"Sum of {n} natural numbers is {s}")


def sum_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + sum_recursive(n-1)

print(f"The sum of first natural numbers is {sum_recursive(2)}")
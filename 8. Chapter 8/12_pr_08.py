# def mul_table(n):
#     for i in range(1,11):
#         print(n*i)

# n=int(input("Enter the value of number :"))
# tab=mul_table(n)
# print(tab)


def mul_table(n):
    for i in range(0,10):
        print(n*(i+1))
        if i == 9:              # this condition avoids printing None at the end
            break

n = int(input("Enter the value of number: "))
mul_table(n)
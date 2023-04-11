# def maximum(num1, num2, num3):
#     if (num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3

# m = maximum(13, 55, 2)
# print("The value of the maximum is " + str(m))

# def max(n1, n2, n3):                      #This is redundant becoz we have max inbuilt function
#     if (n1>n2):
#         if(n1>n3):
#             return n1
#         else:
#             return n3
#     if (n2>n3):
#        return n2
#     else:
#         return n3

a=int(input("Enter the 1st number: \n"))
b=int(input("Enter the 2nd number: \n"))
c=int(input("Enter the 3rd number: \n"))
m=max(a, b, c)                              # max is inbuilt function 
print(f"The value of the maximum is {m}")
   
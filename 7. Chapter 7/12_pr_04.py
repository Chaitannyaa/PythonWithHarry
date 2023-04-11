# num = int(input("Enter the number: "))
# prime = True

# for i in range(2, num):
#     if(num%i == 0):
#         prime = False
#         break
# if prime:
#     print("This number is Prime")
# else:
#     print("This number is not Prime")

num = int(input("Enter your number: "))
Prime=True
for i in range(2, num):
    if (num%i==0):
        Prime=False
        break
if Prime:
    print("Your number is Prime")
else:
    print("Your number is Not Prime")
# def farh(cel):
#     return (cel *(9/5)) + 32

# c = 0
# f = farh(c)
# print("Fahreheit Temperature is " + str(f))

def farh(cel):
    return cel *(9/5) + 32

c=int(input("Enter your tempreture in Celsius : "))
f=farh(c)
print("Tempreture in fahrenhiet is " + str(f))
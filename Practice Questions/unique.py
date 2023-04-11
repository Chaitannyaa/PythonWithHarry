n=int(input("Enter the number"))
list=[]
x=n
while n>0:
    rem=n%10
    list.append(rem)
    n=n//10
for i in list:
    if list.count(i)>1:
        print(x, "Number is not unique")
        break
else:
    print("Number is unique")


try:
    a = int(input("Enter a number: "))
    b = 2 + a
    print(b)
    c = 1/a
    print(c)

except TypeError as e:
    print("Please enter the integer value")

except ValueError as e:
    print("Please Enter a valid value") 

except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0") 

print("Thanks for using this code!")
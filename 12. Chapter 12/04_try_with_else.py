try:
    i = int(input("Enter a number: "))
    c = 1/i
    print(c)
except Exception as e:
    print(f"its not allowed {e}")
else:
    print("We were successful")
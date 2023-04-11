try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()          # Its terminates below except finally condition
else:
    print("Check")  # Its printed only if try is successful
finally:
    print("We are done")    # its printed irrespective of anything

print("Thanks for using the program")   # its printed if break or exit is not present/executed
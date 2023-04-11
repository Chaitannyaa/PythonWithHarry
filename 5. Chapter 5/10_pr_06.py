# favLang = {}
# a = input("Enter your favorite language Shubham\n")
# b = input("Enter your favorite language Ankit\n")
# c = input("Enter your favorite language Sonali\n")
# d = input("Enter your favorite language Harshita\n")
# favLang['shubham'] = a
# favLang['ankit'] = b
# favLang['sonali'] = c
# favLang['harshita'] = d

# print(favLang)

# favLang = {}

# a = input("Enter your favourate langauge Krishna :\n")
# b = input("Enter your favourate langauge Keshava :\n")
# c = input("Enter your favourate langauge Madhava :\n")
# d = input("Enter your favourate langauge Govinda :\n")

# favLang['Krishna'] = a
# favLang['Keshava'] = b
# favLang['Madhava'] = c
# favLang['Govinda'] = d

# print(favLang)

i=1
myDict = {}
while i<5:
    key = input(f"Enter the name of user {i}: ")
    value = input(f"Enter the favourate langauge of {key} : ")
    myDict.update({key:value})
    i=i+1
print(myDict)

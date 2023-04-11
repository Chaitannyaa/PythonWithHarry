
# using for loop

with open("log.txt") as f:
    for i in range(1, 40): #For loop can be used when length of content is known
        content=f.readline()
        if 'python' in content.lower():
            print("Python is present in file")
            print(f"Python word is present on line number {i}")


# using while loop

content=True
i = 1
with open('log.txt', 'r') as f:
    while content:
        content=f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"python is present in this content at line No-{i}")
        i+=1

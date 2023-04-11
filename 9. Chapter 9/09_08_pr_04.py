# with open("sample.txt") as f:
#     content = f.read()

# content = content.replace("donkey", "$%^@$^#")

# with open("sample.txt", "w") as f:
#     f.write(content)

with open("sample.txt", 'r') as f:
    content=f.read()
    content=content.lower()

content = content.replace('horse', '#$#$#')

with open("sample.txt", 'w') as f:
    f.write(content)
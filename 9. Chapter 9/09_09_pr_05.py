words = ["horse", "kaddu", "mote"]

# with open("sample.txt") as f:
#     content = f.read()


# for word in words:
#     content = content.replace(word, "$%^@$^#")
#     with open("sample.txt", "w") as f:
#         f.write(content)
with open("sample.txt", 'r') as f:
    content=f.read()
    content=content.lower()
for word in words:
    content = content.replace(word, "#$#$#")

with open("sample.txt", 'w') as f:
    f.write(content)
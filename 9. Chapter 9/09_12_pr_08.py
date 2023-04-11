# with open("this.txt") as f:
#     content = f.read()

# with open("copy.txt", 'w') as f:
#     f.write(content)


with open('copy.txt', 'r') as f:
    content=f.read()
with open('copied_text.txt', 'w') as f:
    f.write(content)
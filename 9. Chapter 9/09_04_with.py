with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'w') as f:
    a = f.write("me")
print(a)


with open('file1.txt', 'r') as f:
    a = f.read()
    print(a)
with open('file2.txt', 'w') as f:
    b = f.write("Jai shri bageshwar dham ki jai\nSannyasi baba ki jai\nhanuman ji ki jai ho")
    print(str(b))
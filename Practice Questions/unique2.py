n=int(input())
a=len(str(n))
b=len(set(str(n)))
if a==b:
    print('Unique')
else:
    print('not-Unique')

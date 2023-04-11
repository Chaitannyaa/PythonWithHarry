# # Important: This syntax will create an empty dictionary and not an empty set
# a = {}
# print(type(a))

# # An empty set can be created using the below syntax:
# b = set()
# print(type(b))

a = {}
print(type(a))
print(a)

b = set()
print(type(b))
b.add(3)
b.add(1)
b.add((1,2,3))
c=set()
print(b)
print(len(b))
# # Creating an empty set
# b = set()
# print(type(b))

# ## Adding values to an empty set
# b.add(4)
# b.add(4)
# b.add(5)
# b.add(5) # Adding a value repeatedly does not changes a set
# b.add((4, 5, 6))

# ## Accessing Elements
# # b.add({4:5}) # Cannot add list or dictionary to sets
# print(b)

# ## Length of the Set
# print(len(b)) # Prints the length of this set

# ## Removal of an Item
# b.remove(5) # Removes 5 front set b
# # b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
# print(b)

# print(b.pop())
# print(b)

a = set()
print(type(a))
print(a)

a.add(4)
a.add(8)
a.add(9)
print(a)
a.add((4, 5, 6))
print(a)

print(len(a))

a.remove(8)
a.remove((4, 5, 6))
print(a.pop())
print(a)
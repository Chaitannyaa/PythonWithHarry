# from functools import reduce

# sum = lambda a, b: a+b

l = [1, 2, 3, 4, 5, 6]
# val = reduce(sum, l)
# print(val)

from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7]
sum = lambda a, b: a+b
print(reduce(sum, l))

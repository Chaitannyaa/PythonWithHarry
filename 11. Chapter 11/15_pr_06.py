# class Vector:
#     def __init__(self, vec):
#        self.vec = vec
    
#     def __str__(self):
#         return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
 

# v1 = Vector([1, 4, 6])
# v2 = Vector([1, 6, 9])
# print(v1)
# print(v2)

class Vector:

    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        if self.j<0 and self.k>0:
            return f'{self.i}i - {-self.j}j + {self.k}k'
        elif self.k<0 and self.j>0:
            return f'{self.i}i + {self.j}j - {-self.k}k'
        elif self.j<0 and self.k<0:
            return f'{self.i}i - {-self.j}j - {-self.k}k'

v=Vector(12,-12,-32)
print(v)
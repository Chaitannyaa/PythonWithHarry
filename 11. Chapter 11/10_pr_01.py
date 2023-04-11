# class C2dVec:
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"

# class C3dVec(C2dVec):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.kcap = k
    
#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
    
# v2d = C2dVec(1, 3)
# v3d = C3dVec(1, 9, 7)
# print(v2d)
# print(v3d)

class C2DV:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def __str__(self):
        return(f"{self.i}i + {self.j}j")

class C3DV(C2DV):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def __str__(self):
        return(f"{self.i}i + {self.j}j + {self.k}k")

v2d=C2DV(3, 5)
v3d=C3DV(2, 6, 4)
print(v2d)
print(v3d)

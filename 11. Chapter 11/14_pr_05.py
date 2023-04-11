class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        index = 0
        str1 = ""
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, v2):
        newList = []
        for i in range(len(self.vec)):
            newList.append((self.vec[i])+(v2.vec[i]))
        return Vector(newList)

    def __mul__(self, v2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * v2.vec[i]
        return sum

v1 = Vector([2,1,3])
v2 = Vector([3,4,2])
print(v1+v2)
print(v1*v2)
print(v1)
print(v2)


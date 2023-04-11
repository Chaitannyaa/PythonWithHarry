# # (a+bi)(c+di) = (ac−bd) + (ad+bc)i

# class Complex:
#     def __init__(self, r, i):
#         self.real = r 
#         self.imaginary = i

#     def __add__(self, c):
#         return Complex(self.real + c.real, self.imaginary + c.imaginary)
    
#     def __mul__(self, c):
#         mulReal =  self.real*c.real - self.imaginary*c.imaginary
#         mulImg =  self.real*c.imaginary + self.imaginary*c.real
#         return Complex(mulReal, mulImg)

#     def __str__(self):
#         if self.imaginary<0:
#             return f"{self.real} - {-self.imaginary}i"
#         else:
#             return f"{self.real} + {self.imaginary}i"

# c1 = Complex(1, -4)
# c2 = Complex(331, -37)
# print(c1 + c2)
# print(c1 * c2)
# print(c1)

# (a+bi)(c+di)=(ac-bd)(ad+bc)i

# class Complex:
#     def __init__(self, r, i):
#         self.real = r
#         self.imaginery = i

#     def __add__(self, c):
#         return f"{self.real + c.real} + {self.imaginery + c.imaginery}i"

#     def __mul__(self, c):
#         mulReal = (self.real*c.real) - (self.imaginery*c.imaginery)
#         mulImaginery = (self.real*c.imaginery) + (self.imaginery*c.real)
#         return Complex(mulReal, mulImaginery)

#     def __str__(self):
#         if self.imaginery<0:
#             return f"{self.real} - {-self.imaginery}i"
#         else:
#             return f"{self.real} + {self.imaginery}i"

# c1=Complex(2, -4)
# c2=Complex(3, 22)
# print(c1+c2)
# print(c1*c2)
# print(c1)
# print(c2)

class Complex:
    def __init__(self, real, imaginery):
        self.real = real
        self.imaginery = imaginery
    def __str__(self):
        if self.imaginery<0:
            return f"{self.real} - {-self.imaginery}i"
        else:
            return f"{self.real} + {self.imaginery}i"
    def __add__(self, c2):
        add_real = self.real + c2.real
        add_imaginery = self.imaginery + c2.imaginery
        if add_imaginery<0:
            print(f"This is addition of complex numbers : {add_real} - {-add_imaginery}i")
        else:
            print(f"This is addition of complex numbers : {add_real} + {add_imaginery}i")
    # (a+bi)(c+di) = (ac−bd) + (ad+bc)i
    def __mul__(self, c2):
        mul_real = (self.real*c2.real) - (self.imaginery*c2.imaginery)
        mul_imaginery = (self.real*c2.imaginery) + (self.imaginery*c2.real)
        if mul_imaginery<0:
            print(f"This is addition of complex numbers : {mul_real} - {-mul_imaginery}i")
        else:
            print(f"This is addition of complex numbers : {mul_real} + {mul_imaginery}i")

c1 = Complex(2, -3)
c2 = Complex(-4, -2)
print(c1)
print(c2)
c1+c2
c1*c2
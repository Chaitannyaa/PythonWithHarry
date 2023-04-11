# salaryAfterIncrement =  salary * increment

# class Employee:
#     salary = 1000 #These are called properties
#     increment = 1.5
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary*self.increment
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, sai):
#         self.increment = sai/self.salary

# e = Employee()
# print(e.salaryAfterIncrement)

# print(e.increment)
# e.salaryAfterIncrement = 2000
# print(e.increment)

class employee:
    salary = 10000
    increment = 3

    @property
    def salaryafterincrement(self):
        return self.salary*self.increment

    @salaryafterincrement.setter
    def salaryafterincrement(self, value):
        self.increment=value/self.salary

e = employee()
print(e.salary)
print(e.salaryafterincrement)
print(e.increment)
e.salaryafterincrement = 20000
print(e.increment)

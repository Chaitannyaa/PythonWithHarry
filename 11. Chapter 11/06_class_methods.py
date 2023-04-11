# class Employee:
#     company = "Camel"
#     salary = 100
#     location = "Delhi"

#     # def changeSalary(self, sal):
#     #     self.__class__.salary = sal

#     @classmethod
#     def changeSalary(cls, sal):
#         cls.salary = sal

# e = Employee()
# print(e.salary)
# e.changeSalary(455)
# print(e.salary)
# print(Employee.salary)


class Gamer:
    company = "GTA"
    salary = 1200

    def changeSalary(self, sal):
        self.__class__.salary = sal

    @classmethod
    def changeCompany(cls, company):
        cls.company = company

g = Gamer()
print(g.salary)
g.changeSalary(2100)
print(g.salary)

print(g.company)
g.changeCompany("Nike")
print(g.company)

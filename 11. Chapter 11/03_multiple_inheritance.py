class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Employee:
    company = "Visa"
    eCode = 120


class Programmer(Employee,Freelancer):
    name = "Rohit"

p = Programmer()
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.company)
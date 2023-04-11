class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()
sam = Employee()
harry.salary = 300
rajni.salary = 400

print(harry.company)
print(rajni.company)
Employee.company = "YouTube"# Class Attributes can be changed like this
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)
print(sam.salary)

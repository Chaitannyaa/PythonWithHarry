class Employee:
    company = "Google"
    salary = 100
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 100000
sam = Employee()
harry.getSalary() # Employee.getSalary(harry)
Employee.getSalary(harry)
Employee.getSalary(sam)
sam.getSalary()
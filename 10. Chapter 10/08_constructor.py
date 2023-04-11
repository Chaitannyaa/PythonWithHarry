class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!") 

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary} PM")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary} PM\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry = Employee("Harry", 70000, "YouTube")
# harry = Employee() --> This throws an error (missing 3 required positional arguments:)
harry.getDetails()
harry.getSalary("Your Servant")
# harry.salary=120000
# harry.getSalary("yes")
# harry.getDetails()
# Employee.getDetails(harry)
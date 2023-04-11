# class Programmer:
#     company = "Microsoft"

#     def __init__(self, name, product):
#         self.name = name
#         self.product = product

#     def getInfo(self):
#         print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")


# harry = Programmer("Harry", "Skype")
# alka = Programmer("Alka", "GitHub")
# harry.getInfo()
# alka.getInfo()

class Programmer:
    Company="Microsoft"

    def __init__(self, Name, Skillset):
        self.Name=Name
        self.Skillset=Skillset
    def getDetails(self, signature):
        print(f"The name of {self.Company} programmer is {self.Name}\nand his skillsets : {self.Skillset} ")

Chaitannyaa = Programmer("Chaitannyaa", "AWS|Azure|Python|Docker|Kubernetes")
Chaitannyaa.getDetails("Data Analyst")

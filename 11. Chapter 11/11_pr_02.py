# class Animals:
#     animalType = "Mammal"

# class Pets:
#     color = "White"

# class Dog:
#     @staticmethod
#     def bark():
#         print("Bow bow!")

# d  = Dog()
# d.bark()


class Animals:
    animalType = "Mammals"

class Pets:
    colour = "white"

class Dog:
    @staticmethod
    def bark():
        print("Bow bow!")
        from playsound import playsound
        playsound('E:\\PracticePYWH\\Python\\11. Chapter 11\\dog.mp3')

d = Dog()
d.bark()
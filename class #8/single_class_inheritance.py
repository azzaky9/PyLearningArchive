class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Tidak ada subclass yang di implementasi")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


animal = Animal("Buddy")
animal.speak()

dog = Dog("Jonathan") # Combine 2 class jadi satu functionallity
print(dog.speak())
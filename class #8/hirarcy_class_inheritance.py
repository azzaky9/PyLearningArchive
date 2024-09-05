class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Tidak ada subclass yang di implementasi")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


dog = Dog("Joe")
cat = Cat("Marry")

print(dog.speak())
print(cat.speak())




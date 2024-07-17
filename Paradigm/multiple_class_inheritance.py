class Walkable:
    def walk(self):
        return "I can Walk!"

class Swimmable:
    def swim(self):
        return "I can Swim"

class Running:
    def run(self):
        return "I can run!"

class Duck(Walkable, Swimmable):
    def quack(self):
        return "I can quack"

class Ceetah(Walkable, Running):
    def quack(self):
        return "I can run & wal"


duck = Duck()
print(duck.walk())
print(duck.swim())
print(duck.quack())

ceetah = Ceetah()
print(ceetah.walk())
print(ceetah.run())
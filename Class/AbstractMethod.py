from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Car engine start"

    def stop_engine(self):
        return "Car stop engine"

    def drive(self):
        return "Car is driving"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "MotorCycle engine start"

    def stop_engine(self):
        return "MotorCycle engine stop"

    def drive(self):
        return "MotorCycle is driving"

car = Car()

print(car.start_engine())
print(car.drive())
print(car.stop_engine())

motorcyle = Car()

print(motorcyle.start_engine())
print(motorcyle.drive())
print(motorcyle.stop_engine())
class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self.__year = year

    def get_car_info(self):
        print(f"{self._make} {self._model} {self.__year}")

    def update_year(self, year):
        if year > 1:
            self.__year = year
        else:
            raise ValueError("Year must be positive")

my_car = Car("Toyota", "Corolla", 2020)

print(my_car._make)
my_car.update_year(2024)
print(my_car.get_car_info())
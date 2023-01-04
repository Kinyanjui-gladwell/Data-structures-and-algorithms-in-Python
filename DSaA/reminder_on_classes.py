"""This contains classes and functions as a refresher on object oriented programming."""

class Dog():
    """."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def names(self):
        print(self.name.title())

    def ages(self):
        print(self.age)


class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def odometer_reading(self):
        """Return the car's mileage."""
        print(f'This car has {self.odometer} miles on it')

    def update_odometer(self, mileage):
        """update the odometer reading to mileage."""
        self.odometer = mileage

class Battery():
    """."""
    def __init__(self, battery=70):
        self.battery = battery

    def describe_battery(self):
        print(f'This car has a {self.battery}-KwH battery')


class ElectricCar(Car):
    """Initialize attributes of the parent class."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_dog = Dog('willie', 19)
my_dog.names()
my_dog.ages()
print(my_dog.name)
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading()
my_new_car.update_odometer(23)
my_new_car.odometer_reading()
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
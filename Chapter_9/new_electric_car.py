# sometimes you'll want to spread out your classes
# over several modules to keep any one file from
# growing too large and avoid storing unrelated
# classes in the same module. When you store your
# classes in several modules, you may find that a
# class in one module depends on a class in another
# module. When this happens, you can import the
# required class into the first module.

"""A set of classes that can be used to represent electric cars."""

from new_car import Car

class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Reminds us that electric car's don't have gas tanks."""
        print("This car doesn't need a gas tank!")
# if the class you're writing is a specialized version
# of another class you wrote, you can use inheritance
# when one class inherits from another, it automatically
# takes on all the attributes and methods of the first
# class. The original class is called the parent class,
# and the new class is the child class. The child class
# inherits every attribute and method from its parent
# class but is also free to define new attributes and
# methods of its own

# the first task Python has when creating an instance
# from a child class is to assign values to all attributes
# in the parent class. To do this, the __init__() method
# for a child class needs help from its parent class

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    # this method is made to be an example of overriding
    def fill_gas_tank(self):
        """Simulates filling in a cars gas tank."""
        print("All filled up!")
    
# when you create a child class, the parent class must be
# part of the current file and must appear before the child
# class in the file (you can do this by importing, more on
# that later)
# the name of the parent class must be included in parantheses
# in the definition of the child class
# the super() function is a special function that helps Python
# make connections between the parent and child class
# it allows us to use and inherit the __init__() method from
# Car as well as all its attributes

# once you have a child class that inherits from a parent
# class, you can add any new attributes and methods necessary
# to differentiate the child class from the parent class

# for an attribute or method that is not specific to an
# electric car, add it in the Car parent class so that it
# can be used by any class inheriting from Car including
# ElectricCar

# you can override any method from the parent class that
# doesn't fit what you're trying to model with the child
# class. To do this, you define a method in the child class
# with the same name as the method you want to override in
# the parent class. Python will disregard the parent class
# method and only pay attention to the method you define
# in the child class

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        """Gives description of the car's battery"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """Reminds us that electric car's don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

my_car = Car('ford', 'focus', 2019)
my_car.fill_gas_tank()
my_tesla.fill_gas_tank()
print("\n")

# when modeling something from the real world in code,
# you may find that you're adding more and more detail
# to a class. You might recognize that part of one class
# can be written as a separate class. You can break your
# large class into smaller classes that work together

# in this case the variable battery in electrib car is
# now an instance of the Battery class

# we can now add more attributes and methods regarding
# the battery without cluttering the electric car class

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

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
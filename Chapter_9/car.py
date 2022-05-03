# one of the first tasks you'll want to do is modify the
# attributes associated with a particular instance
# you can modify the attributes of an instance directly
# or write methods that update attributes in specific ways

# every attribute in a class needs an initial value, even if
# that value is 0 or an empty string. In some cases, such
# as when setting a default value, it makes sense to specify
# this initial value in the body of the __init__() method;
# if you do this for an attribute, you don't have to include
# a parameter for that attribute

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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# you can change an attribute's value in three ways:
# you can change the value directly through an instance,
# set the value through a method,
# or increment the value through a method

# the simplest way to modify the value an attribute is to
# access the attribute directly through an instance

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# it can help to have methods that update certain attributes
# for you. Instead of accessing the atributes directly, you
# pass the new value to a method that handles the updating
# internally
# we can now include the method update_odometer()

# we can extend the method update_odometer() to do additional
# work every time the odometer reading is modified. Let's add
# a little logic to make sure no one tries to roll back the
# odometer reading

my_new_car.update_odometer(46)
my_new_car.read_odometer()

# sometimes you'll want to increment an attribute's values by
# a certain amount rather than set an entirely new value
# now we can define the method increment_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
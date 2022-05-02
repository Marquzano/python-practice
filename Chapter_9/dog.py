# you can model almost anything using classes. Let's start
# by writing a simple class, dog, that represents a dog

# each instance created from the Dog class will store a name
# and an age, and we'll give each dog the ability to sit() and roll_over()

# a function that's part of a class is a method. Everything
# you learned about functions applies to methods as well;
# the only practical difference for now is the way we'll call methods

# the __init__() method is a special method Python runs automatically
# whenever we create a new instance based on the Dog class.
# this method has two leading underscores and two trailing underscores,
# a convention that helps prevent Python's default method names
# from conflicting with your method names

# the self parameter is required in the method definition,
# and it must come first before the other parameters
# it must be included because when Python calls this __init__()
# method later (to create an instance of Dog), the method call
# will automatically pass the self argument

# every method call associated with a class automatically passes
# self, which is a reference to the instance itself; it gives the 
# individual instance access to the attributes and methods in
# the class

# self.name = name takes the value stored in the parameter name
# and stores it in the variable name, which is then attached to
# the instance being created. 
# variables that are accessible through instances like this are
# called attributes

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")

# think of a class as a set of instructions for how to make an instance.
# the class Dog is a set of instructions that tells Python how
# to make individual instances representing specific dogs

# when Python reads my_dog = Dog('willie', 6), it calls the __init__()
# method in Dog with the arguments 'willie' and 6, notice how we do not
# pass a self; self is pass automatically, so we don't need to pass it
# the __init__() method has no explicit return statement, but Python
# automatically returns an instance representing this dog
# we store the instance in the variable my_dog

# to access the attributes of an instance, you use dot notation

my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
print("\n")

# after we create an instance from the class Dog, we can
# use dot notation to call any method defined in Dog

# to call a method, give the name of the instance and the method
# you want to call, separated by a dot

my_dog.sit()
my_dog.roll_over()
print("\n")

# you can create as many instances from a class as you need
# in this example we create a dog named Willie and a dog named
# Lucy. Each dog is a separate instance with its own set of 
# attributes, capable of the same set of actions

# you can make as many instances from one class as you need
# as long as you give each instance a unique variable name
# or it occupies a unique spot in a list or dictionary

your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("My dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
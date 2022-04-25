# you can pass arguments to your functions in a number of ways
# you can use positional arguments, which need to be in the same order the parameters were written
# you can use keyword arguments, where each argument consists of a variable name and a value;
# and lists and dictionaries of values

# python must match each argument in the function call with a parameter in the function definition
# the simplest way to do this is based on the order of the arguments provided
# values matched up this way are called positional arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

# you can call a function as many times as needed
describe_pet('dog', 'willie')

# order matters in positional arguments
describe_pet('harry', 'hamster')

# because harry is listed first this time it is stored in the parameter animal_type,
# likewise hamster is stored in the parameter animal_type

# a keyword argument is a name-value pair that you pass to a function.
# you directly associate the name and the value within the argument, so when you pass
# the argument to the function, there's no confusion
describe_pet(animal_type="hamster", pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# when writing a function, you can define a default value for each parameter.
# if an argument for a parameter is provided in the function call, Python uses the
# argument value. If not, it uses the parameter's default value

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')

# notice how the order of the parameters has been changed. Since we placed a default value
# for animal_type we must make this the last parameter to be filled since this would still
# be affected by positional arguments. So if it is just called with an argument for pets name
# it can use the default value.
# now if we want to change the value for animal_type, we could do it in the following ways

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')

# it doesn't really matter which calling style you use. As long as your function calls produce
# the output you want, just the style you find easiest to understand.

# when you start to use functions, don't be surprised if you encounter errors about unmatched
# arguments. Unmatched arguments occur when you provide fewer or more arguments than a function
# needs to do its work. i.e.

describe_pet() # this gives an error since we atleast have to give it the positional argument for pet_name
# according to the last function definition that was written
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
    print("My " + animal_type + "'s name is " + pet_name)
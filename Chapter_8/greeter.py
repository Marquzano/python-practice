# this example shows the simplest structure of a function.

def greet_user():
    """Display a simple greeting.""" # this is a docstring
    print("Hello!")

greet_user()
print("\n")

# we can modify the function to take some information
def greet_user(username):
    """Displays a simple greeting to a specified user"""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
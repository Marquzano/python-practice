"""This holds the classes necessary to model a restaurant."""

class Restaurant():
    """The model of a common restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize restaurant attributes"""
        self.name = name
        self.cuisine_type =  cuisine_type

    def describe_restaurant(self):
        """Gives the general overview of the restaurant."""
        print("Name: " + self.name.title())
        print("Cuisine type: " + self.cuisine_type.title())

    def open_restaurant(self):
        """Gives the notification that the restaurant is open."""
        print(self.name.title() + " is open!")
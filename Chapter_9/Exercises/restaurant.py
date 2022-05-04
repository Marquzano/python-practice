

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

restaurant = Restaurant("la mexicana", "mexican")
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n")

restaurant2 = Restaurant("sunflower cafe", "vegan")
restaurant3 = Restaurant("the corner pub", "americana")

restaurant.describe_restaurant()
print("\n")
restaurant2.describe_restaurant()
print("\n")
restaurant3.describe_restaurant()
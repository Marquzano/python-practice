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

class IceCreamStand(Restaurant):
    """A simple model of an ice cream stand."""

    def __init__(self, name, cuisine_type, flavors):
        """Initialized the attributes of the ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Gives a display of the flavors available."""
        print("We have the following flavors: ")
        for flavor in self.flavors:
            print("- " + flavor.title())

flavors = ['moose tracks', 'strawberry', 'mint chocolate chip', 'fudge ripple', 'classic vanilla']
ice_cream_stand = IceCreamStand('chocolate and vanilla', 'frozen desert', flavors)
ice_cream_stand.display_flavors()
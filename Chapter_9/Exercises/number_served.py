class Restaurant():
    """The model of a common restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize restaurant attributes"""
        self.name = name
        self.cuisine_type =  cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Gives the general overview of the restaurant."""
        print("Name: " + self.name.title())
        print("Cuisine type: " + self.cuisine_type.title())

    def open_restaurant(self):
        """Gives the notification that the restaurant is open."""
        print(self.name.title() + " is open!")

    def set_number_served(self, amount):
        """Allows you to set the total amount of guests served."""
        self.number_served = amount

    def increment_number_served(self, increment):
        """Allows you to increment the amount of people served per business day."""
        self.number_served += increment

restaurant = Restaurant('la mexicana', 'mexican')
print("The number of customers the restaurant has served: " + str(restaurant.number_served))
restaurant.number_served = 200
print("The number of customers the restaurant has served: " + str(restaurant.number_served))
print("\n")

restaurant.set_number_served(300)
print("The number of customers the restaurant has served: " + str(restaurant.number_served))
print("\n")

restaurant.increment_number_served(50)
print("The number of customers the restaurant has served: " + str(restaurant.number_served))
class Users():
    """A simple model for user data"""

    def __init__(self, first, last, age, occupation, single):
        """Initialize user attributes"""
        self.first_name = first
        self.last_name = last
        self.age = age
        self.occupation = occupation
        self.single = single
    
    def describe_user(self):
        """Gives a summary of individual user information"""
        full_name = self.first_name.title() + " " + self.last_name.title()
        print(full_name + ":")
        print("- " + str(self.age) + " years old.")
        print("- " + self.occupation.title())
        print("- single? " +  str(self.single()))

    def greet_user(self):
        """Gives a proper greeting to the user"""
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + "!")

# need to finish
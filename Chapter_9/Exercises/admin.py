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
        print("- single? " +  str(self.single))

    def greet_user(self):
        """Gives a proper greeting to the user"""
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + "!")

class Admin(Users):
    """This is a simple model of a user administrator."""

    def __init__(self, first, last, age, occupation, single, privileges):
        """Initializes the attributes of the administrator."""
        super().__init__(first, last, age, occupation, single)
        self.privileges = privileges

    def describe_user(self):
        """Gives a summary of individual user information"""
        full_name = self.first_name.title() + " " + self.last_name.title()
        print(full_name + ":")
        print("- " + str(self.age) + " years old.")
        print("- " + self.occupation.title())
        print("- single? " +  str(self.single))
        print("- admin")
    
    def show_privileges(self):
        """Displays the privileges of the admin."""
        print("These are the privileges you have as an admin:")
        for privilege in self.privileges:
            print("- " + privilege)

privileges = ['can add post', 'can delete post', 'can ban user', 'can view passwords...']
admin = Admin('angel', 'marquez', 24, 'software engineer', False, privileges)
admin.show_privileges()
admin.describe_user()
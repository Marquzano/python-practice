"""Contains the necessary classes to make an admin user."""

from new_users import Users

class Privileges():
    """A simple model of the privileges given to an admin."""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """Displays the privileges of the admin."""
        print("These are the privileges you have as an admin:")
        for privilege in self.privileges:
            print("- " + privilege)

class Admin(Users):
    """This is a simple model of a user administrator."""

    def __init__(self, first, last, age, occupation, single, privileges):
        """Initializes the attributes of the administrator."""
        super().__init__(first, last, age, occupation, single)
        self.privileges = Privileges(privileges)

    def describe_user(self):
        """Gives a summary of individual user information"""
        full_name = self.first_name.title() + " " + self.last_name.title()
        print(full_name + ":")
        print("- " + str(self.age) + " years old.")
        print("- " + self.occupation.title())
        print("- single? " +  str(self.single))
        print("- admin")
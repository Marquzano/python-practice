class Users():
    """A simple model for user data"""

    def __init__(self, first, last, age, occupation, single):
        """Initialize user attributes"""
        self.first_name = first
        self.last_name = last
        self.age = age
        self.occupation = occupation
        self.single = single
        self.login_attempts = 0
    
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
    
    def increment_login_attempts(self):
        """Increments the amount of login attempts during one visit."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Resets the login_attempts after a successful login"""
        self.login_attempts = 0

user = Users('angel', 'marquez', 24, 'software engineer', False)

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print("The number of login attempts so far: " + str(user.login_attempts))
user.reset_login_attempts()
print("The number of login attempts so far: " + str(user.login_attempts))
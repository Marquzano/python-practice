from random import randint

class Die():
    """A simple model of a single die."""

    def __init__(self, sides=6):
        """Initializes the die."""
        self.sides = sides

    def roll_die(self):
        """Rolls the die."""
        side = randint(1, self.sides)
        print(side)

die = Die()

print("This is a 6-sided die.")
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()

die = Die(10)

print("This is a 10-sided die.")
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()

die = Die(20)

print("This is a 20-sided die.")
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
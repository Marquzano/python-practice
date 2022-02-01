#This script will take the alien_colors script further by making it into an if-elif-else chain

# alien_color = 'green' #This will execute the if block
# alien_color = 'yellow' #This will execute the elif block
alien_color = 'red' #This will execute the else block

if alien_color.lower() == 'green':
    print("You receieved 5 points for shooting the " + alien_color + " alien!")
elif alien_color.lower() == 'yellow':
    print("You receieved 10 points for shooting the " + alien_color + " alien!")
else:
    print("You receieved 15 points for shooting the " + alien_color + " alien!")
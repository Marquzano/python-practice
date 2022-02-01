#An example of a simple conditional statement and action

alien_color = 'green'
# alien_color = 'yellow' #This will give us no output

if alien_color.lower() == 'green':
    points = 5
    print("You have recieved: " + str(points) + " points!")
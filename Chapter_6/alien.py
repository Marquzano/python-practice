# this simple dictionary stores information about a particular alien

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print('\n')

# dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print('\n')

# it's sometimes convenient, or even necessary, to start with an empty dictionary
# and then add each new item to it

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
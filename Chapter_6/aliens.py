# sometimes you'll want to store a set of dictionaries in a list
# or a list of items in a dictionary. This is called nesting

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print("\n")

# a more realistic example would involve more than three aliens
# with code that automatically generates each alien

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
print("\n")

# how might you work with a set like this? Imagine that one aspect
# of a game has some aliens changing color and moving faster as the
# game progresses

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# lets show the first 5 aliens now
for alien in aliens[:5]:
    print(alien)
print('...')
print("\n")

# we could go even further

for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# now lets show the first 10
for alien in aliens[:10]:
    print(alien)
print('...')
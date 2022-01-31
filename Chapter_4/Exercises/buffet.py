#A simple script to show the use of tuples

buffet_items = ('lo mein', 'fried rice', 'spring rolls', 'fries', 'garlic bean curd')

print("The available buffet items are the following:")
for item in buffet_items:
    print(item.title())
print('\n')

#Showing that item assignment is not allowed on tuples
# buffet_items[-1] = "beef teriyaki"

buffet_items = ('lo mein', 'fried rice', 'spring rolls', 'sesame buns', 'general tso\'s bean curd')
print('Here is our modified menu for today:')
for item in buffet_items:
    print(item.title())
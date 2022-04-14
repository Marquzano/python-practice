favoritePlaces = {
    'jeorgia': ['e + rose', 'the schermerhorn', 'bridgestone arena'],
    'angel': ['sunflower cafe', 'diskin cider brewery', 'be-hive'],
    'molly': ['the cobra lounge', 'the hyatt'],
}

for name, favoritePlaces in favoritePlaces.items():
    print("\n" + name.title() + "'s favorite places include:")
    for place in favoritePlaces:
        print("\t" + place.title())
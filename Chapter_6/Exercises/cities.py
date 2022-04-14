cities = {
    'nashville': {
        'country': 'united states',
        'population': '689,447',
        'fact': 'Named for Francis Nash, a general of the Continental Army during the American Revolutionary War.',
    },
    'barcelona': {
        'country': 'spain',
        'population': '5,658,472',
        'fact': 'The name Barcelona comes from the Barca family of Carthage who ruled the area in the 3rd century before Christ.',
    },
    'tokyo': {
        'country': 'japan',
        'population': '37,274,000',
        'fact': 'The fact that they\'re located on an island and their population is still that large.',
    },
}

for city, city_info in cities.items():
    print("\n" + city.title() + ":")
    print("\tCountry: " + city_info['country'].title())
    print("\tPopulation: " + city_info['population'])
    print("And a fact: " + "\n" + city_info['fact'])
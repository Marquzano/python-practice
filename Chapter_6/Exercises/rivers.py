rivers = {'nile': 'egypt',
        'rio grande': 'mexico',
        'mississippi river': 'united states',
        }

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
print("\n")

print("The dictionary includes the following rivers:")
for river in rivers:
    print(river.title())
print("\n")

print("The dicitonary includes the following countries:")
for country in rivers.values():
    print(country.title())
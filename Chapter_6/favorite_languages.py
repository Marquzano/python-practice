# this shows us how to format dictionaries of similar objects
# this example also shows you how to break up a long print statement over several lines.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")
print("\n")

# here we update the code now that we know how to loop through dictionaries

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
    language.title() + ".")
print("\n")

# we could also choose to just loop through the keys of the dictionary
# for example lets show the names of all the people who took our "poll"

for name in favorite_languages.keys():
    print(name.title())
print("\n")

# looping through the keys of a dictionary is actually the default when looping through a dictionary
# so the following would yield the same result

for name in favorite_languages:
    print(name.title())
print("\n")

# you can access the value associated with any key you care about
# inside the loop by using the current key

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")
print("\n")

# you can also use the keys() method to find out if a particular
# person was polled

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# the keys() method is not just for looping: it actually returns a list
# of all the keys, and we are simply checking if erin is in this list
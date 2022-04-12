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
print("\n")

# the keys() method is not just for looping: it actually returns a list
# of all the keys, and we are simply checking if erin is in this list

# when printing the contents of a dictionary they are never in any particular
# order, but we can create a sense of order
# i.e.

for name in favorite_languages.keys():
    print(name.title() + ", thank you for taking the poll.")
print("\n")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
print("\n")

# if you are primarily interested in the values that a dictionary
# contains, you can use the values() method to return a list of values
# without any keys

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print("\n")

# in the previous example we are able to print each value that is in the
# dictionary, but notice how it is reptitive. This is fine for small sample data
# but would become very repititve in larger samples, so we can use set to handle duplicates

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# when you wrap set() around a list that contains duplicate items, Python identifies
# the unique items in the list and builds a set from those items

# you can nest a list inside a dictionary any time you want more than one value to be
# associated with a single key in a dictionary
# i.e. if we were to store each person's responses in a list, people could choose more
# than one favorite language

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
print("\n")

# we could refine this code a little further by distinguishing those who have a 
# singular favorite language

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        language = languages[0]
        print("\n" + name.title() + "'s favorite language is " + language.title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
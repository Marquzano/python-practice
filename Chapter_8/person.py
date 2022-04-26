# a function can return any kind of value you need it to
# including more complicated data structures like lists and dictionaries

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name,}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# we can easily extend this function to accept optional values like a middle name,
# an age, an occupation, or any other information you want to store about a person
# i.e.

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name,}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)

# or you could've done:
# musician = build_person('jimi', 'hendrix', age=27)
# or
# musician = build_person('jimi', 'hendrix', age='27')
# or even
# musician = build_person('jimi', 'hendrix', '27')
# it doesn't much matter if you give it an int or string
# or if you give it as a positional or keyword argument
# depends entirely on your writing style and the way you wish to format data
# just make it consistent and understandable
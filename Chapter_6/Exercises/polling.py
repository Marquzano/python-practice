favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

needPollers = ['jen', 'angel', 'edward', 'phil', 'emily', 'josh']

for name in needPollers:
    if name in favorite_languages:
        print(name.title() + ", thank you for taking the poll!")
    else:
        print(name.title() + ", please take our poll!")
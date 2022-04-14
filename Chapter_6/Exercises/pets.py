lex = {
    'name': 'lex',
    'animal': 'dog',
    'owners': ['jordan', 'dru'],
}
luna = {
    'name': 'luna',
    'animal': 'dog',
    'owners': ['dru', 'jordan'],
}
samuel = {
    'name': 'samuel',
    'animal': 'cat',
    'owners': ['jesse'],
}
sasha = {
    'name': 'sasha',
    'animal': 'cat',
    'owners': ['jordan', 'dru'],
}
hazel = {
    'name': 'hazel',
    'animal': 'cat',
    'owners': ['dru', 'jordan'],
}
cash = {
    'name': 'cash',
    'animal': 'dog',
    'owners': ['jimmy', 'julie'],
}
arvi = {
    'name': 'arvi',
    'animal': 'dog',
    'owners': ['jeorgia', 'angel'],
}
theo = {
    'name': 'theo',
    'animal': 'dog',
    'owners': ['sarah'],
}
abu = {
    'name': 'abu',
    'animal': 'cat',
    'owners': ['amanda'],
}
kristoff = {
    'name': 'kristoff',
    'animal': 'cat',
    'owners': ['amanda'],
}

pets = [lex, luna, samuel, sasha, hazel, arvi, cash, theo, abu, kristoff]

for pet in pets:
    if len(pet['owners']) > 1:
        print("\n" + pet['name'].title() + " is a " + pet['animal'] + ".")
        print("They are owned by " + pet['owners'][0].title() + " and " + pet['owners'][1].title() + ".")
    else:
        print("\n" + pet['name'].title() + " is a " + pet['animal'] + ".")
        print("They are owned by " + pet['owners'][0].title() + ".")
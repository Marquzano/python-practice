# this exercise is an extension of person.py

person = {'first_name': 'jose', 'last_name': 'paz amaya', 'age': 23, 'city': 'philadelphia'}
person1 = {'first_name': 'emily', 'last_name': 'davis', 'age': 25, 'city': 'nashville'}
person2 = {'first_name': 'katherine', 'last_name': 'large', 'age': 24, 'city': 'denver'}

people = [person, person1, person2]

for person in people:
    print("My friends name is " +
        person['first_name'].title() + " " +
        person['last_name'].title() + ".\n" +
        "They are " + str(person['age']) + " years old" +
        " and lives in " + person['city'].title() + '.')
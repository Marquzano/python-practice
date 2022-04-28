# this script shows that modifying lists can occur in functions

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i]

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

magicians = ['nicolas flamel', 'roger bacon', 'michael scot']

show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
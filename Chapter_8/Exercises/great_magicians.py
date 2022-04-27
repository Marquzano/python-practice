# this needs to be fixed
def make_great(magicians):
    i = 0
    length = len(magicians)
    while i < length:
        modifiedMagician = "The Great " + magicians[i]
        magicians.append(modifiedMagician)
        magicians.remove(magicians[i])
        i += 1

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

magicians = ['nicolas flamel', 'roger bacon', 'michael scot']

make_great(magicians)
show_magicians(magicians)
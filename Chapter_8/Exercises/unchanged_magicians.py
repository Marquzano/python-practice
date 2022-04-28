# this list shows us how to avoid modifying our original list by sending a copy to the function instead

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i]
    return magicians

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

magicians = ['nicolas flamel', 'roger bacon', 'michael scot']

greatMagicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(greatMagicians)
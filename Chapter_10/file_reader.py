# an incredible amount of data is available in text files.
# text files can contain all kinds of data and more. Reading
# from a file is particularly useful in data analysis apps
# but it's also applicable to any situation in which you 
# want to analyze or modify information stored in a file.
# when you want to work with the information in a text
# file, the first step is to read the file into memory
# you can read the entire contents of a file, or you can
# work through the file one line at a time.

# to begin we have created a text file in a folder called
# pi_digits.txt. we will first open it and read it's entire
# contents

# to do any work with a file, even just printing its
# contents, you first need to open the file to access it.
# open() takes only one argument, the name of the file you
# want to open. open() returns a file object and stores it
# in file_object in this example. the keyword `with` closes
# the file once access to it is no longer needed

with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
print("\n")

# when you are reading from a file, you'll want to examine
# each line of the file. You might be looking for certain
# information in the file, or you might want to modify the
# text in the file in some way. You can use a for loop on
# the file object to examine each line from a file one at
# a time.

filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
print("\n")

# when you use `with`, the file object returned by open()
# is only available inside the `with` block that contains
# it. If you want to retain access to a file's contents
# outside the `with` block, you can store the file's line
# in a list inside the block and then work with that list

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print("\n")

# after you've read a file into memory, you can do
# whatever you want with that data

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
# one of the simplest ways to save data is to write
# it to a file, the output will still be available
# after you close the terminal containing your
# programs output. You can examine output after a
# program finishes running, and you can share the
# output files with others as well. You can also
# write programs that read the text back into memory
# and work with it again later

# to write text to a file, you need to call open()
# with a second argument telling Python that you
# want to write to a file.

# the second argument in open() tells Python that
# we want to open the file in write mode. You can
# open a file in read mode ('r'), write mode ('w'),
# append mode ('a'), or a mode that allows you to
# read and write to the file ('r+'). If you omit
# the mode argument, Python opens the file in
# read-only mode by default.

# the open() function automatically creates the file
# you're writing to if it doesn't already exist.
# However, be careful opening a file in write mode
# ('w') becuase if the file does exist, Python will
# erase the file before returning the file object

# python can only write strings to a text file, so 
# if you are working with numerical data make sure
# to convert it to string before you write it the file

filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# the write() function doesn't add any newlines to
# the text you write. So if you write more than one
# line without including newline characters, your 
# file may not look the way you want it to

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

# including newlines in your write() statements makes
# each string appear on its own line

# you can also use spaces, tab characters, and
# blank lines to format your output, just as
# you've been doing with terminal-based output

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# if you want to add content to a file instead of
# writing over existing content, you can open the
# file in append mode. When you open a file in
# append mode, Python doesn't erase the file before
# returning the file object. Any lines you write to
# the file will be added at the end of the file. If
# the file doesn't exist yet, Python will create an
# empty file for you.

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
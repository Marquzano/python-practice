# one common issue when working with files is
# handling missing files. The file you're looking
# for might be in a different location, the 
# filename may be misspelled, or the file may not
# exist at all. You can handle all of these
# situations in a straightfoward way with a try-
# except block.

# this file does not exist
filename = 'alice.txt'

# with open(filename) as f_obj:
#     contents = f_obj.read()

# the last line of the traceback reports a
# FileNotFoundError: this is the exception Python
# creates when it can't find the file it's trying 
# to open. In this example, the open() function
# produces the error

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
print("\n")

# you can analyze text files containing entire
# books. We'll use the string method split(), which
# can build a list of words from a string. The split()
# method separates a string into parts wherever it
# finds a space and stores all the parts of the string
# in a list.

# I have added the text to the text_files folder
# got UTF-8 text file from www.gutenburg.org
filename = 'text_files/alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
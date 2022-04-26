# now that we have a further understanding of functions we can modify
# the greeter script to greet people more formally

# you can use functions with all the Python structures you've learned
# about so far. Let's use the get_formatted_name() function in a while
# loop to greet users more formally.


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()

# this is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# we want to be able to quit as easily as possible, so each prompt
# should offer a way to quit.

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
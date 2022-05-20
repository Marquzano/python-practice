# Python uses special objects called exceptions
# to manage errors that arise during a program's
# execution. Whenever an error occurs that makes
# Python unsure what to do next, it creates an
# exception object. If you write code that
# handles the exception, the program will
# continue running. If you don't handle the 
# exception, the program will halt and show a
# traceback, which includes a report of the 
# exception that was raised.

# exceptions are handled with try-except blocks.
# a try-except block asks Python to do something
# , but it also tells Python what to do if an
# exception is raised.

# lets look at a simple error that causes Python
# to raise an exception. The following creates a
# ZeroDvisionError exception object.

# print(5/0)

# when you think an error may occur, you can
# write a try-except block to handle the exception
# that might be raised. Here's what a try-except
# block for handling the ZeroDivisionError
# exception looks like:

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print("\n")

# if the code in a try block works, Python skips
# over the except block. If the code in the try
# block causes an error, Python looks for an
# except block whose error matches the one that
# was raised and runs the code in that block

# handling errors is especially important when
# the program has more work to do after the
# error occurs. This happens often in programs
# that prompt users for input. If the program
# responds to invalid input appropriately, it
# can prompt for more valid input instead of
# crashing

# NOTE: it's not a good idea to let users see
# tracebacks. In a malicious setting, attackers
# will learn more than you want them to know
# from a traceback. i.e. they'll know the name
# of your program file, and they'll see a part
# of your code that isn't working properly. A
# skilled attacker can sometimes use this info
# to determine which kind of attacks to use
# against your code.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("\nYou can't divide by 0!")
    else:
        print(answer)

# any code that depends on the try block 
# succeeding is added to the else block. In
# this case if the division operation is
# successful, we use the else block to print the
# result.
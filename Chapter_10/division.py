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

# if the code in a try block works, Python skips
# over the except block. If the code in the try
# block causes an error, Python looks for an
# except block whose error matches the one that
# was raised and runs the code in that block
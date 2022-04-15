# this exercise is simply an update on glossary.py now that we know how to loop through dicitionaries

terms = {'print': "This key word is used to print a string or any other value or object to the terminal",
        'list': "This key word is a template to help make a list and takes several argument values",
        'for': "This key word allows you to loop through certain commands given a condition",
        'if': "This key word allows you to evaluate a conditional statement down to a boolean value",
        'del': "This key word is used to delete values in arrays and dicitionaries permanently",
        }

for word, definition in terms.items():
    print(word + ": " + definition + ".\n")
from collections import OrderedDict

terms = OrderedDict()

terms['print'] = "This key word is used to print a string or any other value or object to the terminal"
terms['list'] = "This key word is a template to help make a list and takes several argument values"
terms['for'] = "This key word allows you to loop through certain commands given a condition"
terms['if'] = "This key word allows you to evaluate a conditional statement down to a boolean value"
terms['del'] = "This key word is used to delete values in arrays and dicitionaries permanently"

for word, definition in terms.items():
    print(word + ": " + definition + ".\n")
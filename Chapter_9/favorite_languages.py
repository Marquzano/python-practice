# the python standard library is a set of modules
# included in every Python installation. Now that
# you have a basic understanding of how classes
# work, you can start to use modules like these
# that other programmers have written.

# you can use any function or class in the standard
# library by including a simple import statement at
# the top of your file. Let's look at one class,
# OrderedDict, from the module collections.

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
    language.title() + ".")

# favorite_languages.py already fulfills this, but
# apparently the significance of OrderedDict is that
# it keeps the items in a dictionary in order of when
# they were added to the dictionary.

# as you learn more about the standard library, you'll
# become familiar with a number of modules like this
# that help you handle common situations.

# you can also download modules from external sources.
# eventually we'll need external modules to complete a 
# project
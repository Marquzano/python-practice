# this shows us how to format dictionaries of similar objects
# this example also shows you how to break up a long print statement over several lines.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")
# I am trying to figure out the best way to check if a string
# is composed of a single letter

ini_list = ['a', 'aaaaaaa', 'aaaabaaa', 'aaaaaaa', 'aaaaaaaa']

# count comparison
for i in ini_list:
    if i.count(i[0]) == len(i):
        print("String {} have all characters same".format(i))
    else:
        print("String {} don't have all characters same".format(i))

wit = i.count(i[0])
print(wit)

# string comparison
for i in ini_list:
    print(i)
    if i == len(i)*i[0]:
        print("String {} have all characters same".format(i))
    else:
        print("String {} don't have all characters same".format(i))

wit = len(i)*i[0]
print(wit)

# I believe I understand the string comparison a bit more
# essentially what is happening in line 19 is that it checks
# to see if the list is equal to another list of the same length
# made up of the first letter in the list
# this will be useful for repeated_string.py in Hackerrank_code
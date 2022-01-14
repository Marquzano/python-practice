#This is a script to showcase all of the functionality a list is capable of performing
#append, insert, delete, pop, remove, sort, sorted, reverse, length
languages = ['spanish', 'english', 'german', 'arabic']

print('This is the original list of languages I would like to learn:')
print(languages)

#append a language that you would like to add on your list
print('\n')
print('I have added another language I would like to learn.')
languages.append('finnish')
print(languages)

#insert a language that you want to learn more eagerly than the rest
print('\n')
print('I will now insert a language that I am eager to learn.')
languages.insert(2, 'japanese')
print(languages)

#delete a language you're least likely to learn
print('\n')
print('I am going to delete a language I don\'t think I wil get to.')
del languages[4]
print(languages)

#pop languages you've already learned
print('\n')
print('I will also remove languages from the list that I have already learned.')
learned1 = languages.pop(0)
learned2 = languages.pop(0)
print(languages)
print('That\'s right I\'ve already learned ' + learned1 + " and " + learned2 + '!')
print('I got a head start on those ;)')

#remove a language you think might be too difficult
print('\n')
print('I will remove another language due to it\'s difficulty')
hard_lang = 'finnish'
languages.remove(hard_lang)
print(languages)
print('I am sorry to say ' + hard_lang + ' might be too challenging')
print('I\'ll definitely try my best one day though.')

#show the length of the list of languages you have yet to learn
print('\n')
print('So this leaves me with ' + str(len(languages)) + ' languages to really dedicate myself to soon.')

#sort them here
print('\n')
print('This is what that list looks like sorted.')
print(sorted(languages))
print('This is the original list')
print(languages)
print('This is it permanently sorted.')
languages.sort()
print(languages)
print('This is the sorted list in reverse.')
languages.reverse()
print(languages)
print('Here it is sorted back to normal.')
languages.reverse()
print(languages)

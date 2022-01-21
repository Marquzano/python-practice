#In this script we will introduce the concept of copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
#Here we have made a copy of the list my_foods and saved it to friend_foods
friend_foods = my_foods[:]

#To prove that these two are independent and different lists lets append a different item to both
#This right here will also show why friend_foods = my_foods is not the proper way to copy a list, since this would make both variables point to the same list reference
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
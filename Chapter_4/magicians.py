#This script introduces the use of loops in the context of lists
magicians = ['alice', 'david', 'carolina']

#This demonstrates the use of a temporary variable to hold the data in the list
#as it iterates
for magician in magicians:
    print(magician)
print('\n')

#This example shows us that we are able to do more to the value within the for loop
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    #For every indented line there is more functionality we could add
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

#Any lines that come after the for loop will be executed only once
#These lines are out of the for loop since they are not indented
print("Thank you, everyone. That was a great magic show!\n")

#The more common errors with loops or other blocks of code are indentation errors like the following
#Uncomment the blocks of code to see the errors/results

#This creates an error since there isn't an indent where there needs to be one
# for magician in magicians:
# print(magician)

#In this example there will not be an error but will cause issues
# for magician in magicians:
#     print(magician.title() + ", that was a great trick")
# print("I can't wait to see your next trick, " + magician.title() + ".\n")

#An unnecessary indent will also cause an error
# message = "Hello Python World!"
#     print(message)

#Unnecessarily indenting after a for loop can also cause problems
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")

#     print("Thank you, everyone. That was a great magic show!\n")

#Forgetting the colon when making a block of code will cause a syntax error
# for magician in magicians
#     print(magician)
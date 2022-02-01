#if-elif-else chains are powerful when you need to execute a single action for a specific condition
#However, sometimes it's important to check all of the conditions of interest
#This technique makes sense when more than one condition could be true
#Lets take the toppings example from earlier

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#This example wouldn't work if it were an if-elif chain
#Once the first conditional statement is met the other block of code aren't executed even if they are true
#So mushrooms would be added but extra cheese would be left out

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#If more than one block of code needs to run, use a series of independent if statements
#Here we show that conditional statements can be used to execute specific blocks of code for items in a for loop

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
print("\n")

#Up until now we have assumed that the list is not empty
#We can use if statements to help determine this before we continue with the other blocks of code

requested_toppings = []

#If you pass a list the condition will pass True if there is at least one item in the list
#If it is an empty list then it passes as False
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
print("\n")

#Lets expand on the use of lists with conditional statements and use 2 lists

available_toppings = ['mushrooms', 'olives','green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
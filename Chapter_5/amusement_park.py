#Often you'll need to test more than two possible situations
#To evaluate these we can use Python's if-elif-else syntax

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
print("\n")

#In this situation we could just set the price and output the value in a single print

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
print("\n")

#You can use multiple elif (else if) statements as a chain

age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")
print("\n")

#We can also omit the else block
#Sometimes it makes sense to just catch the leftover cases in the last elif statement
#This also makes the code more readable

age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")
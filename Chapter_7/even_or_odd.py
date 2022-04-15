# here we will introduce the modulo operator
# unlike division where we can see how many times
# a number fits into another, the modulo operator 
# lets us know the remainder
# if a number is divisible by another then it returns 0
# otherwise it returns how many are left

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# if you're using Python 2.7, use raw_input() instead of input()
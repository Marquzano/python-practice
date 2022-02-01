#This script will describe the more complex uses of if statements
#The conditional statement can be any kind of conditional statement

age = 19
if age >= 18:
    #If statements work in the same way for loops do when it comes to indented blocks of code
    #This block will only be executed if the conditional statement is true otherwise it's not executed
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
print("\n")

#If statments are not only able to perform actions when a condition is met
#But it can also perform actions if a condition isn't met with the following else statement
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
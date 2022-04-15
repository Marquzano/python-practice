number = int(input("Give me a number, and I'll let you know if it is a multiple of 10: "))

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")
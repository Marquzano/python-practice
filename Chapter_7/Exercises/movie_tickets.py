prompt = "How old are you? "

while True:
    age = int(input(prompt))
    if age < 3:
        print("The ticket is free")
        break
    elif 3 <= age <= 12:
        print("The ticket is $10")
        break
    elif age > 12:
        print("The ticket is $15")
        break
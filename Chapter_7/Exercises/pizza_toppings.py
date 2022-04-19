
prompt = "\nPlease enter the toppings you'd like on your pizza:"
prompt += "\n(Enter 'quit' to exit the selection board.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("\nWe'll add " + topping.title())
        print("Anything else?")
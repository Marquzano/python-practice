sandwich_orders = ['pastrami on rye', 'mediterranean', 'italian sub', 'philly cheese steak sub']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("\nI made your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

print("\nThese sandwiches were made:")
for sandwich in finished_sandwiches:
    print("\t"+ sandwich)
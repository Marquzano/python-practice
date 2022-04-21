sandwich_orders = ['pastrami', 'mediterranean', 'italian sub', 'philly cheese steak sub', 'pastrami', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("\nI made your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

print("\nThese sandwiches were made:")
for sandwich in finished_sandwiches:
    print("\t"+ sandwich)
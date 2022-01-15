#Here is how you would create a list of the first 10 square numbers into a list

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)
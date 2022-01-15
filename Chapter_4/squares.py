#Here is how you would create a list of the first 10 square numbers into a list

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)
print('\n')

#You can accomplish the above faster and easier in one line using list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
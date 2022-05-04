

def repeatedString(s, n):
    """Returns the amount of a's present in the infinitely repeated string."""
    dividend = n // len(s) # this will hold the amount of times we completely repeat s
    mod = n % len(s) # this holds the length of which we will splice s on the last repitition
    countA = 0 # this holds the amount of a's in s
    countModA = 0 # this will hold the amount of a's held in the incomplete repition of s
    amount = 0 # this will hold the final total amount
    # check if a is not in s in which case return 0
    if 'a' not in s:
        return 0
    # check if s is only composed of a's in which case return n
    if s == len(s)*'a':
        return n
    # go through s once to get the number of a's
    # and then multiply by n//s
    for letter in s:
        if letter == 'a':
            countA += 1
    # get the dividend = n//s and get its modulus = n % len(s)
    # go through a splice of s of length modulus to get the
    # remaining a's in the sequence
    for letter in s[:mod]:
        if letter == 'a':
            countModA += 1
    amount = countA * dividend + countModA

    return amount

# beacuse n = 15 this is the repeated string 'abaababaababaab'
# the expected result is 9
s = 'abaab'
n = 15
result = repeatedString(s, n)
print(result)
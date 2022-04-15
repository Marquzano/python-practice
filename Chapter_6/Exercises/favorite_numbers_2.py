# this exercise is a modifcation of favoriteNumbers.py so that each person can have multiple favorite numbers

favorite_numbers = {'angel': [4, 1],
                    'emily': [124],
                    'ryan': [9, 69],
                    'dylan': [100, 2, 96],
                    'jose': [64, 16],
                    }

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print("\n" + name.title() + "'s favorite numbers are:")
        for number in numbers:
            print("\t" + str(number))
    else:
        print("\n" + name.title() + "'s favorite number is " + str(numbers[0]) + ".")
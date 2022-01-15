#More practice using lists
boards = ['skateboard', 'longboard', 'cruiser', 'e-board']

skate_message = boards[0] + 's are made to do tricks mainly and cruise.\n'

long_message = boards[1] + 's are mostly for cruising and dancing.\n'

cruiser_message = boards[2] + 's bring the best of both worlds from ' + boards[0] + 'ing to ' + boards[1] + 'ing.\n'

e_message = boards[3] + 's scare me...\n'

print(skate_message + long_message + cruiser_message + e_message)
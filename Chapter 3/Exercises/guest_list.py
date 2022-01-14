#List exercise
dinner_guests = []

dinner_guests.append('michael faraday')
dinner_guests.append('elon musk')
dinner_guests.append('steve jobs')

print("Dear " + dinner_guests[0].title() + ",\nI admire your work and tenacity. You are invited to a dinner at my home on September 10th at 6 PM CST.\nhumbly,\n\tAngel Marquez\n")
print("Dear " + dinner_guests[1].title() + ",\nI admire your work and tenacity. You are invited to a dinner at my home on September 10th at 6 PM CST.\nhumbly,\n\tAngel Marquez\n")
print("Dear " + dinner_guests[2].title() + ",\nI admire your work and tenacity. You are invited to a dinner at my home on September 10th at 6 PM CST.\nhumbly,\n\tAngel Marquez\n")

#Modified version of the list to adjust for guests who are not able to make it
unable_to_attend = 'michael faraday'
print(unable_to_attend.title() + ' will not be able to attend the dinner party.')
dinner_guests.remove(unable_to_attend)

dinner_guests.append('michio kaku')

print("Dear " + dinner_guests[0].title() + ",\nI admire your work and tenacity. You are invited to a dinner at my home on September 10th at 6 PM CST.\nhumbly,\n\tAngel Marquez\n")
print("Dear " + dinner_guests[1].title() + ",\nI admire your work and tenacity. You are invited to a dinner at my home on September 10th at 6 PM CST.\nhumbly,\n\tAngel Marquez\n")
print("Dear " + dinner_guests[2].title() + ",\nI admire your work and tenacity. You are invited to a dinner at my home on September 10th at 6 PM CST.\nhumbly,\n\tAngel Marquez\n")

#Adding three more guests using insert and append method
print('\n\n\n')

dinner_guests.append('neil degrasse tyson')
dinner_guests.insert(0, 'robin williams')
dinner_guests.insert(2, 'richard feynman')

print("Dear " + dinner_guests[0].title() + ",\nI admire your work and tenacity. You are invited to a dinner at my home on September 10th at 6 PM CST.\nhumbly,\n\tAngel Marquez\n")
print("Dear " + dinner_guests[1].title() + ",\nI admire your work and tenacity. You are invited to a dinner at my home on September 10th at 6 PM CST.\nhumbly,\n\tAngel Marquez\n")
print("Dear " + dinner_guests[2].title() + ",\nI admire your work and tenacity. You are invited to a dinner at my home on September 10th at 6 PM CST.\nhumbly,\n\tAngel Marquez\n")
print("Dear " + dinner_guests[3].title() + ",\nI admire your work and tenacity. You are invited to a dinner at my home on September 10th at 6 PM CST.\nhumbly,\n\tAngel Marquez\n")
print("Dear " + dinner_guests[4].title() + ",\nI admire your work and tenacity. You are invited to a dinner at my home on September 10th at 6 PM CST.\nhumbly,\n\tAngel Marquez\n")
print("Dear " + dinner_guests[5].title() + ",\nI admire your work and tenacity. You are invited to a dinner at my home on September 10th at 6 PM CST.\nhumbly,\n\tAngel Marquez\n")
print('\n\n\n')

#Shrinking guest list
print('As it turns out the table we have reserved for the occasion will not be ready.\nDue to the news we will now only be able to invite 2 guests.')

uninvited_guest = dinner_guests.pop()
print('Dear ' + uninvited_guest.title() + ',\nI regret to inform you that you have been uninvited from the dinner party.\nMy sincerest apologies,\n\tAngel Marquez')
uninvited_guest = dinner_guests.pop()
print('Dear ' + uninvited_guest.title() + ',\nI regret to inform you that you have been uninvited from the dinner party.\nMy sincerest apologies,\n\tAngel Marquez')
uninvited_guest = dinner_guests.pop()
print('Dear ' + uninvited_guest.title() + ',\nI regret to inform you that you have been uninvited from the dinner party.\nMy sincerest apologies,\n\tAngel Marquez')
uninvited_guest = dinner_guests.pop()
print('Dear ' + uninvited_guest.title() + ',\nI regret to inform you that you have been uninvited from the dinner party.\nMy sincerest apologies,\n\tAngel Marquez')
print('\n')
print('Dear ' + dinner_guests[0].title() + ',\nI am thankful to let you know that everything is still in line for you to attend the dinner party on the 10th of September.\nSee you soon,\n\tAngel Marquez')
print('Dear ' + dinner_guests[1].title() + ',\nI am thankful to let you know that everything is still in line for you to attend the dinner party on the 10th of September.\nSee you soon,\n\tAngel Marquez')

del dinner_guests[0]
del dinner_guests[0]

print(dinner_guests)
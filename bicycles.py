#This is an example of a list and it's output when printed
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print("\n")

#Lists are ordered so you can access individual items from the list by using its index
print(bicycles[0] + "\n")

#Depending on the data in the lists certain methods can be performed on the list if it is indexed
print(bicycles[1].title() + "\n")

#The index starts at 0 so the fourth item in the list would be index 3
#Also python can access the last items in a list with negative numbers 
print(bicycles[1] + "\n" + bicycles[3] + "\n" + bicycles[-1] + "\n" + bicycles[-2])
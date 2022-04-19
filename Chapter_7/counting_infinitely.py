# every while loop needs a way to stop running so it won't continue to run forever.
# i.e. this counting loop should count from 1 to 5

x = 1
while x <= 5:
    print(x)
    x = 1 # here we made a "mistake" by not making it x += 1

# this while loop will print 1 infinitely unless it is terminated
# you can stop it with a keyboard interrupt ^C
# this program helps us to play a game of jumping on clouds as efficiently as possible
# the objective of the game is to get to the last "cloud" without jumping on a thundercloud
# you can jump to another cloud if it's index is only 1 or 2 away
# regular clouds are 0 and thunderclouds are represented by 1
# find the minimum amount of jumps needed to get to the last cloud

# attempt 2
def jumpingOnClouds(c):
    playing = True
    jumps = 0
    position = 0
    while playing:
        if (position + 1) == len(c):
            playing = False
        elif position + 2 <= len(c) - 1 and  c[position + 2] == 0: # apparently if you test its bound right before you check the value in that index it will help avoid that error
            position +=  2
            jumps += 1  
        elif c[position + 1] == 0:
            position += 1
            jumps += 1
    return jumps


c = [0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(c))
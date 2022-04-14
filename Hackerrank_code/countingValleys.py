# a hiker keeps track of every step they take on their hike
# for every step he takes he notes it as an uphill or downhill step
# a mountain is an uphill step followed by a downhill step (must return to sea level)
# a valley is a downhill step followed by an uphill step (must return to sea level)
# given a sequence of steps we must determine how many valleys they have traversed

def countingValleys(steps, path):
    # we still have to keep track of the mountains
    # to determine when they reach sea level to see
    # if they go lower to keep count of valleys
    elevation = 0
    valleys = 0
    for elevStep in samplePath:
        # maybe we could use a counter
        # if elevation > 0 it's on a mountain
        # if elevation == 0 it's at sea level
        # if elevation < 0 it's in a valley
        # in this last condition we can iterate valleys
        print(elevStep)



samplePath = 'UUDDDDUUDU'
countingValleys(len(samplePath), samplePath)
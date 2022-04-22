# a hiker keeps track of every step they take on their hike
# for every step he takes he notes it as an uphill or downhill step
# a mountain is an uphill step followed by a downhill step (must return to sea level)
# a valley is a downhill step followed by an uphill step (must return to sea level)
# given a sequence of steps we must determine how many valleys they have traversed

def countingValleys(steps, path):
    elevation = 0
    valleys = 0 
    for elevStep in path:
        # we will determine the elevation like this:
        if elevStep == 'U':
            elevation += 1
        elif elevStep == 'D':
            elevation -= 1
        # here we determine if we've stepped into a valley
        if elevation == -1 and elevStep == 'D':
            valleys += 1
    return valleys



samplePath = 'UUDDDDUUDU'
numOfValleys = countingValleys(len(samplePath), samplePath)
print("You traversed " + str(numOfValleys) + " valleys.")
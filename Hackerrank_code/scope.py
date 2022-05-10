class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        arr = self.__elements
        maxInt = max(arr)
        minInt = min(arr)
        maxDifference = abs(maxInt - minInt)
        self.maximumDifference = maxDifference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
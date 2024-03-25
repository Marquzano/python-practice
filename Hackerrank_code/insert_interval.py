# You are given an array of non-overlapping intervals intervals where intervals[i] = [start[i], end[i]] 
# represent the start and the end of the ith interval and intervals is sorted in ascending order by start[i]. 
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by start[i] and 
# intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# what I have so far
class Solution:
    def insert(self, intervals, newInterval):
        # case 1:
        # the interval to be inserted has no overlap in either start or end
        # find the index to insert it appropriately
        # case 2:
        # the interval overlaps in either start or end with other present intervals
        # 
        leftIndex = 0
        rightIndex = 0

        for intval in intervals:
            start = intval[0]
            end = intval[1]
            # check if it is just an overlap
            if start <= newInterval[0] <= end and start <= newInterval[1] <= end:
                return intervals
            # check if start is an overlap but end is not
                # determine index of overlap for start
                # determine the start value of intval
            # check if start is not an overlap but end is 
                # determine index of overlap for end
                # determine the end value of intval

# there are 4 different possiblities when merging
# () is an interval already in intervals
# {} is the interval needing to be inserted
# ({)}, ()
# ({)(})
# (), {(})
# {()}
# If no merge is required then there is only one solution
# (), {}, ()
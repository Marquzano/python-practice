# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. 
# If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, 
# an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# need to review over O notation as sorted function may have exceeded O(log(n)) runtime

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # since we do not have to worry about identifying
        # multiple peaks, we will simply return the index
        # for the largest peak in the array
        sortedNums = sorted(nums)
        # here we find the largest value in the array
        # thus the largest peak
        peak = sortedNums[-1]

        # return the index of the peak
        return nums.index(peak)
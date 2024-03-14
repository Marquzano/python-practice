# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]] 

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

# incomplete solution below
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # we need to include the following sets
        # one of all available nums
        # one empty set
        output = [[], nums]

        # a set which contains only one of each available num
        for num in nums:
            if [num] not in output:
                output.append([num])
                
        # the rest of the unique subsets
        # use the individual number subsets already in output to
        # construct the remaining subsets
        # there are only ever going to be 10 numbers or less in nums
        # will have to use that to further flesh out the brute force solution

        return output
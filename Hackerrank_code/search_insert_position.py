# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# what I have so far
# seems to return None value when given input:
# nums = [1], target = 0
# check this testcase out and fix
class Solution:
    def searchInsert(self, nums, target) -> int:
        # if it is already in nums then return its index
        if target in nums:
            return nums.index(target)

        # if not determine where it belongs in nums
        for i in range(len(nums) - 1):
            # if it is less than the first value then return index 0
            if i == 0 and target < nums[0]:
                return i
            # check if it is between two nums return the index
            # that would be between them if it was inserted
            elif nums[i] < target < nums[i+1]:
                return i+1
            # if we are at the last value then it has to be greater than it
            # after the above case so we return the length of nums which is
            # always one more than the actual last index
            elif (i+1) == (len(nums) - 1):
                return len(nums)
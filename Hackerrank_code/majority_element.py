# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # how to determine the number of instances of a value in nums?

        # this solution only holds true if there are only 2 unique values in nums
        num = nums[0]
        numberOfInstances = 0
        while num in nums:
            try:
                nums.pop(num)
            except:
                break
            numberOfInstances += 1
        
        if numberOfInstances >= (len(nums)/2):
            return num
        else:
            return nums[0]
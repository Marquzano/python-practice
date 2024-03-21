# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums) -> int:
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

# 2nd solution/attempt
class Solution2:
    def majorityElement(self, nums) -> int:
        numOfInstances = {}
        
        # here we determine the total number of instances
        # for all values in nums
        for num in nums:
            if num in numOfInstances.keys():
                numOfInstances[num] += 1
            else:
                numOfInstances[num] = 1

        # we go through each item from the aforementioned dictionary
        for num,instance in numOfInstances.items():
            # return the value which makes up at least half or more
            # of the array nums
            if instance >= (len(nums)/2):
                return num

    
soln = Solution2
nums = [2,2,1,1,1,2,2]
result = soln.majorityElement(soln, nums)
print(result)
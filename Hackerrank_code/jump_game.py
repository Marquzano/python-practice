# You are given an integer array nums. You are initially positioned at the array's first index, and each element 
# in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, 
# which makes it impossible to reach the last index.

# my complete solution
class Solution:
    def canJump(self, nums) -> bool:
        jumpLength = nums[0]
        i = 0

        while i <= len(nums):
            if (jumpLength + i) >= (len(nums) - 1):
                return True
            else:
                i += jumpLength
                jumpLength = nums[i]
                if jumpLength == 0:
                    return False
                
# test case
# nums = [2,5,0,0]
# Expected output is true for this?
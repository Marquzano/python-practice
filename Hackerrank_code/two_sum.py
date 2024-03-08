# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a dictionary to keep track of the indices
        # run a for loop to go through each number in nums
        # for i check if each number j adds up to the target
        # for each index that doesn't work pop it from nums
        indices = {}
        i = 0 
        resultIndices = []

        for i in range(len(nums) - 1):
            if nums[i] in indices.keys():
                indices[nums[i]].append(i)
            else: 
                indices[nums[i]] = [i]
            i += 1

        j = 0
        k = 0
        # need to review the loops here
        # worked on this very quickly
        # may want to redo the solution
        # passes example 1 but not 2 or 3
        for j in range(len(nums) - 1):
            for k in range(len(nums)):
                if nums[j] + nums[k] == target:
                    if nums[j] == nums[k] and j != k:
                        resultIndices.append(indices[nums[j]][0])
                        resultIndices.append(indices[nums[j]][1])
                        return resultIndices
                    else:
                        resultIndices.append(indices[nums[j]][0])
                        resultIndices.append(indices[nums[k]][0])
                        return resultIndices
                k += 1
            nums.pop(j)
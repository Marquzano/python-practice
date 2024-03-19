# Given an integer array nums and an integer k, return true if 
# there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true

# this does not pass the test cases
# will need to check how to optimize after making proper solutions

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        # define a dictionary
        # keys: value
        # value: array of it's indices

        numberOfInstances = {}
        i = 0

        # populate numberOfInstances
        for i in range(len(nums)):
            if nums[i] not in numberOfInstances.keys():
                numberOfInstances[nums[i]] = [i]
            elif nums[i] in numberOfInstances.keys():
                numberOfInstances[nums[i]].append(i)
            i += 1

        # now go through each value in numberOfInstances
        for indices in numberOfInstances.values():
            # pop the first value and get the absolute difference
            # from the remaining values in the array
            # while indices still has at least one value in it
            while len(indices) >= 2:
                check = indices.pop(0)
                for value in indices:
                    if abs(value - check) <= k:
                        return True
        
        return False

# test case
soln = Solution
nums = [1,2,3,4,1]
k = 3
result = soln.containsNearbyDuplicate(soln,nums,k)
print(result)
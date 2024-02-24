# Given an integer array nums and an integer k, return true if 
# there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true

# this does not pass the test cases
# will need to check how to optimize after making proper solutions

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # define a dictionary
        # keys: value
        # value: list where 
        # [0] = number of instances
        # [1,i] = indeces of the value in list nums

        numberOfInstances = {}
        # manNums = nums

        # to populate the dictionary
        # go through the values of nums/manNums
        i = 0
        while i <= len(nums) - 1:
            # take value
            # check if the value is already in numberOfInstances
            if nums[i] in numberOfInstances.keys():
                # it is so:
                # we iterate +1 on [0]
                # append the index to the list
                numberOfInstances[nums[i]][0] += 1
                numberOfInstances[nums[i]].append(i)
            else:
                numberOfInstances[nums[i]] = [1,i]
            i += 1
        
        # see if this populates correctly
        print(numberOfInstances)

        # check values[0] if there are duplicates
        # if there are go through [1,i]
        # calculate the absolute differences
        # until one is <= k
        for arr in numberOfInstances.values():
            if arr[0] == 1:
                continue
            else:
                i = 0
                j = 0
                for i in range(1,len(arr)-2):
                    for j in range(2,len(arr)-1):
                        if abs(arr[i] - arr[j]) <= k:
                            return True
                        else:
                            j += 1
                    i += 1

        return False
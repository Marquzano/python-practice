# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

# what I have so far
class Solution:
    def combinationSum2(self, candidates, target: int):
        output = []

        # first remove all candidates that are greater than target
        for num in candidates:
            if num > target:
                candidates.remove(num)

        # sort the candidates array
        candidates = candidates.sorted()
        # create a sampleArr list that contains the first value popped from candidates
        sampleArr = []
        i = 0
        # add values to the sample array as long as their total sum is less than the target
        for i  in range(len(candidates) - 1):
            sampleArr.append(candidates[i])
            if sampleArr.sum() == target:
                if sampleArr not in output:
                    output.append(sampleArr)
                    i = 0
                # need to reset sampleArr to continue with the "current" first value
                # but also move on to the next value after the last solution
        # if you reach the target value before you go through all the nums in candidates
        # append the sampleArr to outputs
        # and continue with the first value once more until you make it to the end of the list
        # without another possible solution
        # each time you make it to the end of the list remove the first value to move on to
        # others
        # each time you find a solution check that it is not already in output array

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates 
# where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency
# of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than
# 150 combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

# here is what I have so far
# for some reason Example 1 is not working even though I believe it should
# output keeps getting returned empty
# need to also look into problems listed in lines 57 - 61
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # brute force this for now
        # for each number determine quotient and remainder needed to sum to target
        i = 0
        j = 0
        output = []

        for i in range(len(candidates) - 1):
            # this handles cases where a single candidate
            # can sum up to target
            if target % candidates[i] == 0:
                newArr = []
                while j <= (target / candidates[i]):
                    newArr.append(candidates[i])
                    j += 1
                j = 0
                output.append(newArr)
            # this handles cases where a certain set of
            # candidates can sum up to target
            if (target % candidates[i]) in candidates:
                newArr = []
                while j <= (target // candidates[i]):
                    newArr.append(candidates[i])
                    j += 1
                j = 0
                index = candidates.index(target % candidates[i])
                newArr.append(candidates[index])
                output.append(newArr)
            # need to write code which goes through each possible addition
            # need to include also where a combination of other candidates
            # plus a multiple of one other candidate example [1,2,3] target = 14
            # [[1,2,2,3,3,3]]
            # this may need to be included in the logic from above
            i += 1

        return output
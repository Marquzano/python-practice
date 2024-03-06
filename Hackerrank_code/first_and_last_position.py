# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# my suboptimal solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # make output variable
        positions = []
        ogLength = len(nums)

        # check if the target is in nums at all
        if target not in nums:
            return [-1,-1]
        else:
            positions.append(nums.index(target))
            nums.remove(target)
            # check if there is even another position to note
            if target not in nums:
                # if not, return the same index twice as first and last position
                positions.append(positions[0])
                return positions
            nums.sort(reverse = True)
            positions.append(abs(nums.index(target) - len(nums)))
        
        return positions
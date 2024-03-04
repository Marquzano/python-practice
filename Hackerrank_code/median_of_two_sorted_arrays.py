# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge both lists
        mergedArr = sorted(nums1 + nums2)
        # determine if it makes up an odd or even overall list
        # if odd then take cieling(len(combinedArr)/2) - 1
        if len(mergedArr)%2 != 0:
            # give the value from above as the index
            return mergedArr[ceil(len(mergedArr)/2) - 1]
        # if even take average of len/2 and len/2 - 1
        else:
            index1 = ceil(len(mergedArr)/2)
            index2 = ceil(len(mergedArr)/2) - 1
            return (mergedArr[index1] + mergedArr[index2])/ 2
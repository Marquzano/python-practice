# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # create helper variables
        indexHaystack = 0
        indexNeedle = 0
        indexForOutput = 0
        # we need to first determine if needle is in haystack
        if needle not in haystack:
        # if it is not in return -  1
            return -1
        # else we continue by turning both into lists
        # could also be simplified by the use of regex
        else:
            haystack = list(haystack)
            needle = list(needle)
            # iterate through the needle list
            # once it iterates through once we confirm
            # that the needle is in the haystack
            while indexNeedle in range(len(needle) - 1):
                if haystack[indexHaystack] == needle[indexNeedle] and indexNeedle == 0:
                    # note index if this is true and needleIndex == 0
                    indexForOutput = indexHaystack
                    indexHaystack += 1
                    indexNeedle += 1
                elif haystack[indexHaystack] != needle[indexNeedle]:
                    indexNeedle = 0
                elif haystack[indexHaystack] == needle[indexNeedle]:
                    indexHaystack += 1
                    indexNeedle += 1
                elif haystack[indexHaystack] != needle[indexNeedle]:
                    indexHaystack += 1
            return indexForOutput
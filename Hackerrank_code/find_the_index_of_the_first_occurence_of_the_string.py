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

# what I have so far
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        output = -1
        if needle not in haystack:
            return output
        else:
            haystack = list(haystack)
            needle = list(needle)
            # here we go through the hay stack
            for i in range(len(haystack)-1):
                for j in range(len(needle)-1):
                    if haystack[i] == needle[j] and j == 0:
                        output = i
                        i += 1
                        j += 1
                    elif haystack[i] == needle[j] and j == (len(needle)-1):
                        # not sure why it isn't arriving to this line
                        return output
                    elif haystack[i] == needle[j]:
                        i += 1
                        j += 1
                    else:
                        i += 1
                        j = 0
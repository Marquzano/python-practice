# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # use a dictionary
        # create one to one relations in the dictionary
        # key: each letter from s
        # value: each letter from t

        pairings = {}
        listS = list(s)
        listT = list(t)
        i = 0
        # determine if it is isomorphic within this loop
        # getting key error on line 28
        while i in range(len(listS) - 1):
            if listS[i] not in pairings.keys():
                pairings[listS[i]] = listT[i]
            elif pairings[listS[i]] != listT[i]:
                    return False
            i += 1

        return True
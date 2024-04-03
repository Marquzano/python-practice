# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# my complete brute force solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make a dictionary of both strings
        # key is the character
        # value is the integer value of the number of instances in the string
        sDict = {}
        tDict = {}
        for character in s:
            if character in sDict.keys():
                sDict[character] += 1
            else:
                sDict[character] = 1
        for character in t:
            if character in tDict.keys():
                tDict[character] += 1
            else:
                tDict[character] = 1
        
        for character,inst in tDict.items():
            if len(tDict.keys()) != len(sDict.keys()):
                return False
            if character not in sDict.keys():
                return False
            if inst != sDict[character]:
                return False
        
        return True
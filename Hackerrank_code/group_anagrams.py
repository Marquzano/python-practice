# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# what I have so far
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create empty output list
        # we will be appending the groups of anagrams
        outputList = []
        # create a dictionary
        # key: length of the strings
        # value: list of strings of the same length defined by key
        lengthWords = makeLengthWords(strs)

        # now go through each key and it's values
        for length,words in lengthWords:
            for word in words:
                if len(outputList) == 0:
                    outputList.append([word])
                elif word in outputList[]
                # slight hiccup here
                # I am wanting to check the first word of the last input
                # in outputList but the word that it is like could be
                # earlier in outputList
                # I'd have to write another for loop to check each word
                # in the lists...

    def makeLengthWords(self, strs):
        lengthWords = {}
        for word in strs:
            if len(word) not in lengthWords.keys():
                lengthWords[len(word)] = [word]
            else:
                lengthWords[len(word)].append(word)

        return lengthWords

    # def checkAnagram():
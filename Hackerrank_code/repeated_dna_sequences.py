# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences 
# (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

# what I have so far
# further notes taken on notepad
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        # needs to be made up of 10 characters
        # needs to occur more than once in the sequence
        output = []

        # we could split the string after every 10th character
        # no
        # we could get a sample string of the first ten characters
        # compare it to the original string
        i = 0
        j = 9
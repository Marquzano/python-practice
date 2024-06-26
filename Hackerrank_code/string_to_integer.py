# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# The algorithim for myAtoi(string s) is as follows:

# 1. Read in and ignore any leading whitespace.
# 2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This
# determines if the final resulat is negative or positive respectively. Assume the result is positive if neither is present.
# 3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# 4. Convert these digits into an integer (i.e. "123" -> 123. "0032" -> 32). If no digits were read, then the integer is 0. Change
# the sign as necessary (from step 2)>
# 5. If the integer is out the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range.
# Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
# 6. Return the integer as the final result.

# Note:
# Only the space character " " is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

# Example 1:
# Input: s = "42"
# Output: 42
# Explanation: The underlined characters are what is read in, the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read beacause there is neither a '-' nor '+')
#          ^
# Step 3: "42"
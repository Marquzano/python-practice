# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

# incomplete, suboptimal, apparent bug regarding number 0
# conversion from str to int logic is flawed need to work further
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # need to convert str to int using my own method
        # take list of each num
        # refer to dictionary of numbers to determine the correct int
        # refer to a reversed order list of either number to
        # determine their place in the integer
        # add them up and give the integer presentation for the next step
        numbers = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        listNum1 = sorted(list(num1), reverse=True)
        listNum2 = sorted(list(num2), reverse=True)
        i = 0
        int1 = 0
        int2 = 0
        for i in range(len(listNum1) - 1):
            if listNum1[i] in numbers.keys():
                place = 10^i
                int1 += (numbers[listNum1[i]] * place)
            i += 1
        i = 0
        for i in range(len(listNum2) - 1):
            if listNum2[i] in numbers.keys():
                place = 10^i
                int2 += (numbers[listNum2[i]] * place)
            i += 1
        # from here we can see that the conversion logic from above is flawed
        # print("Num1: " + num1 + " int1: " + str(int1))
        # print("Num2: " + num2 + " int2: " + str(int2))
        # print("\n")
        # get the product of the two numbers
        product = int1 * int2

        # return the str typecast of the product
        return str(product)
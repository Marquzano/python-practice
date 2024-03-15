# You are given an integer array height of length n. There are n vertical lines drawn such that 
# the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# below is what I have so far
# seems to work but I need to optimize further
# need to make sense of the j index
class Solution:
    def maxArea(self, height) -> int:
        # identify the index of the greatest height in height arr
        # I will write the brute force solution first
        areas = []
        i = 0
        j = 0
        for i in range(len(height) - 1):
            j = i + 1 # need to figure out why j is not indexing properly from here
            for j in range(len(height)):
                if height[i] > height[j]:
                    area = (height[i] - (height[i] - height[j])) * (j - i)
                    # debugging
                    # print('area: ' + str(area))
                    # print('i: ' + str(i) + ', j: ' + str(j))
                    # print('height i: ' + str(height[i]))
                    # print('height j: ' + str(height[j]))
                    # print('distance x : ' + str(j - i))
                    # print('\n')
                else:
                    area = (height[j] - (height[j] - height[i])) * (j - i)
                    # debugging
                    # print('area: ' + str(area))
                    # print('i: ' + str(i) + ', j: ' + str(j))
                    # print('height i: ' + str(height[i]))
                    # print('height j: ' + str(height[j]))
                    # print('distance x : ' + str(j - i))
                    # print('\n')
                areas.append(area)
                j += 1
            i += 1
        
        # print(areas)
        maxArea = max(areas)
        return maxArea

# test code
# output should be 120
soln = Solution
output = soln.maxArea(soln,[4,10,2,5,9,6,6,10,8,5,7,1,2,10,4,3,6,3,5,4])
print(output)
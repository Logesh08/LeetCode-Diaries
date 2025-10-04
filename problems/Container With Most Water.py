
# LeetCode Problem 11: Container With Most Water
# Problem link: https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

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
 

# Constraints:

# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4


# THis is my second solution to the problem.
# I used two pointers to solve the problem.
# It got O(n) time complexity and O(1) space complexity.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height)-1

        while left < right:
            width = right - left
            length = min(height[left],height[right])

            area = max(area, width*length)


            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return area
    

# This is my first solution to the problem.
# It got TLE cuz its O(n^2) solution.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = len(height)
        for i in range(l):
            for j in range(i+1,l):
                ans = max(ans, (j-i) * min(height[i],height[j]) )

        return ans
    



## Resolved same problem in Oct 4 2025
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = left = 0
        right = len(height) - 1
        maxHeight = max(height)
        
        while left < right:
            width = right - left
            area = max(area, min(height[left], height[right]) * width)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            if maxHeight * width < area:
                break       
        
        return area
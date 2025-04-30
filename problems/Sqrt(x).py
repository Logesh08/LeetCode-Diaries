# LeetCode Problem 69: Sqrt(x)
# https://leetcode.com/problems/sqrtx/



# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

# Constraints:

# 0 <= x <= 2^31 - 1





# I realised something, I can use binary search to find the square root of a number.
# Because they are asking for a whole nubmber only, genrally square of x is x*x
# Meaning the root will be y which will be y*y <= x
# If we solve that, then it's our victory

class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x 
        ans = 0

        while start <= end:

            mid = (start + end) // 2
            root = mid * mid

            if root <= x:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1

        return ans

# Beats 100% of the submissions
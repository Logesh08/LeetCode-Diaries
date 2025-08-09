# LeetCode Problem 231. Power of Two
# https://leetcode.com/problems/power-of-two


# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

#  
# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1

# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16

# Example 3:

# Input: n = 3
# Output: false

#  
# Constraints:

# 	-231 <= n <= 231 - 1

#  
# Follow up: Could you solve it without loops/recursion?




# First approach with loop
# The concept here is we need to divide by 2 until its divisible,
# If the number is finally 1, it's valid. Cuz anything that is divisible by 2
# will end up there!

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return 1  # Need to do cuz constraints includes negative numbers
        while n % 2:
            n //= 2
        return n == 1
    


# THis method works because any valid number should be able to divide
# the maximum number of the 32 bit int
	
class Solution:
	def isPowerOfTwo(self, n: int) -> bool:
		return n > 0 and (1073741824 % n == 0)
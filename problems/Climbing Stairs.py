# LeetCode Problem 70: Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/


# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45




# Beats 100% of the submissons
# Guess I'm starting to learn dp

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,2]
        if n <= 2:
            return dp[n-1 ]
        
        for i in range(2,n):
            dp.append(dp[i-1]+dp[i-2])

        return dp[-1]


# Without dp List
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp1,dp2 = 1,2
        for i in range(2,n):
            dp1,dp2 = dp2,dp1+dp2

        return dp2

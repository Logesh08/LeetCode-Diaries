# LeetCode Problem 838: Push Dominoes
# https://leetcode.com/problems/push-dominoes/


# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

# Example 1:


# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 1000




# My solution beats 100% of the submissons
# Runtime 0ms

# I was not able to acheive it because i was returning return dp[-1] % MODULO
# But because of this we will always be processing a very huge number

# Instead we can do the mod in the loop and just return the dp[-1]


class Solution:
    def numTilings(self, n: int) -> int:
        MODULO = 10**9 + 7

        dp = [1,2,5]
        if n in [1,2,3]:
            return dp[n-1]
        
        for i in range(3,n):
            dp.append((2*dp[i-1] + dp[i-3]) % MODULO)

        return dp[-1] 
    



# I can do the same without using the dp array
# I can just use 3 variables to store the last 3 values


class Solution:
    def numTilings(self, n: int) -> int:
        MODULO = 10**9 + 7

        dp1, dp2, dp3 = 1, 2, 5
        if n in [1,2,3]:
            return dp1 if n == 1 else dp2 if n == 2 else dp3
        
        for i in range(3,n):
            dp1, dp2, dp3 = dp2, dp3, (2*dp3 + dp1) % MODULO

        return dp3
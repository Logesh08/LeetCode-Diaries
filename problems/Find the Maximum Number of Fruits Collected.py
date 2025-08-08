# LeetCode Problem 3363: Find the Maximum Number of Fruits Collected
# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected



# There is a game dungeon comprised of n x n rooms arranged in a grid.

# You are given a 2D array fruits of size n x n, where fruits[i][j] represents the number of fruits in the room (i, j). Three children will play in the game dungeon, with initial positions at the corner rooms (0, 0), (0, n - 1), and (n - 1, 0).

# The children will make exactly n - 1 moves according to the following rules to reach the room (n - 1, n - 1):

# The child starting from (0, 0) must move from their current room (i, j) to one of the rooms (i + 1, j + 1), (i + 1, j), and (i, j + 1) if the target room exists.
# The child starting from (0, n - 1) must move from their current room (i, j) to one of the rooms (i + 1, j - 1), (i + 1, j), and (i + 1, j + 1) if the target room exists.
# The child starting from (n - 1, 0) must move from their current room (i, j) to one of the rooms (i - 1, j + 1), (i, j + 1), and (i + 1, j + 1) if the target room exists.
# When a child enters a room, they will collect all the fruits there. If two or more children enter the same room, only one child will collect the fruits, and the room will be emptied after they leave.

# Return the maximum number of fruits the children can collect from the dungeon.

 

# Example 1:

# Input: fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]

# Output: 100

# Explanation:



# In this example:

# The 1st child (green) moves on the path (0,0) -> (1,1) -> (2,2) -> (3, 3).
# The 2nd child (red) moves on the path (0,3) -> (1,2) -> (2,3) -> (3, 3).
# The 3rd child (blue) moves on the path (3,0) -> (3,1) -> (3,2) -> (3, 3).
# In total they collect 1 + 6 + 11 + 16 + 4 + 8 + 12 + 13 + 14 + 15 = 100 fruits.

# Example 2:

# Input: fruits = [[1,1],[1,1]]

# Output: 4

# Explanation:

# In this example:

# The 1st child moves on the path (0,0) -> (1,1).
# The 2nd child moves on the path (0,1) -> (1,1).
# The 3rd child moves on the path (1,0) -> (1,1).
# In total they collect 1 + 1 + 1 + 1 = 4 fruits.

 

# Constraints:

# 2 <= n == fruits.length == fruits[i].length <= 1000
# 0 <= fruits[i][j] <= 1000



# My initial approach using 2D dp array

from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits[0])
        maxFruits = 0

        # For child at 0,0
        for i in range(n):
            maxFruits += fruits[i][i]
            fruits[i][i] = 0

        dp = [[float("-inf")]*(n+1) for _ in range(n+1)]   # I'm doing n+1 so that we can skip checking the boundary condition

        dp[n-1][0] = fruits[n-1][0]
        dp[0][n-1] = fruits[0][n-1]

        # # For child at n-1,0 accend
        # for j in range(1,n//2 + n%2):
        #     for i in range(n-1,n-j-2,-1):
        #         print(fruits[i][j],end=' ')
        #         # dp update here
        #     print()

        # print()

        # # For child at n-1,0 decend
        # ctr = 0
        # for j in range(n//2 + n%2,n):
        #     for i in range(n//2 + ctr,n):
        #         print(fruits[i][j],end=' ')
        #         # dp update here
        #     ctr += 1
        #     print()


        # For child at n-1,0
        dp[n-1][0] = fruits[n-1][0]
        for j in range(1, n-1):
            i_start = max(n-1-j, j+1)
            for i in range(i_start, n):
                dp[i][j] = fruits[i][j] + max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])

        maxFruits += dp[n-1][n-2]

        # For child at 0,n-1
        dp[0][n-1] = fruits[0][n-1]
        for i in range(1, n-1):
            j_start = max(n-1-i, i+1)
            for j in range(j_start, n):
                dp[i][j] = fruits[i][j] + max(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])

        maxFruits += dp[n-2][n-1]
        

        return maxFruits
    



# Same program using 1D dp array
# But we need to use 2 buffers because in each iteration we need to use the previous row's values



class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits[0])
        maxFruits = 0

        # For child at 0,0
        for i in range(n):
            maxFruits += fruits[i][i]
            fruits[i][i] = 0

        dp = [float("-inf")]*(n+1)

        # For child at n-1,0
        dp[n-1] = fruits[n-1][0]
        for j in range(1, n-1):
            i_start = max(n-1-j, j+1)
            dp2 = dp[:]
            for i in range(i_start, n):
                dp[i] = fruits[i][j] + max(dp2[i-1],dp2[i],dp2[i+1])

        maxFruits += dp[n-1]

        dp = [float("-inf")]*(n+1)

        # For child at 0,n-1
        dp[n-1] = fruits[0][n-1]
        for i in range(1, n-1):
            j_start = max(n-1-i, i+1)
            dp2 = dp[:]
            for j in range(j_start, n):
                dp[j] = fruits[i][j] + max(dp2[j-1],dp2[j],dp2[j+1])

        maxFruits += dp[n-1]
        

        return maxFruits
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
        

        print(maxFruits)
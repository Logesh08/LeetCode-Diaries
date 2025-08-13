# Practice one, im ditching it for a better start
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MODULO = 10**9 + 7
        exps = []
        cur = i = 1
        while cur <= n:
            exps.append(cur)
            i += 1
            cur = i ** x

        return exps

# print(Solution().numberOfWays(160,3))

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MODULO = 10**9 + 7

        pows = []
        i = 1
        while i ** x <= n:
            pows.append(i ** x)
            i += 1

        print(pows)
        dp = [0] * (n+1)
        dp[0] = 1
        print(dp)

        for p in pows:
            for s in range(n,p-1,-1):
                dp[s] = (dp[s] + dp[s-p])
                print(dp)

        return dp[n] % MODULO
    

print(Solution().numberOfWays(5,1))
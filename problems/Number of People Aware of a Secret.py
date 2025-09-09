class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MODULO = 10**9 + 7

        dp = [0] * (n+1)
        dp[1] = 1

        activeSpreaders = 0
        for day in range(2,n+1):
            if day > delay:
                activeSpreaders = activeSpreaders + dp[day-delay]
            if day > forget:
                activeSpreaders = activeSpreaders - dp[day-forget]
            dp[day] = activeSpreaders
        ans = sum(dp[n-forget+1:n+1])

        return ans % MODULO
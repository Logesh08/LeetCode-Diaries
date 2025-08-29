# Failed cuz of TLE
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        i = 1
        ans = 0
        while 1 <= i <= n:
            j = 1
            while 1 <= j <= m:
                if (i+j)%2:
                    ans += 1
                j += 1
            i += 1

        return ans
    

# Proper solution:
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (n * m) // 2
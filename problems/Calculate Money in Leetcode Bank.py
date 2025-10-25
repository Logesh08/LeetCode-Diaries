class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        ctr = 1
        mon = 2

        for i in range(1,n+1):
            ans += ctr
            print(ctr)
            if i%7==0:
                ctr = mon
                mon += 1
            else:
                ctr += 1
        return ans

    
print(Solution().totalMoney(7))
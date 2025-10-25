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
    


class Solution:
    def triSum(self, n: int) -> int:
        return (n * (n + 1)) >> 1

    def totalMoney(self, days: int) -> int:
        nWeeks, rDays = divmod(days, 7)        
        return self.triSum(days) - 42 * self.triSum(nWeeks - 1) - 6 * nWeeks * rDays


    
print(Solution().totalMoney(7))
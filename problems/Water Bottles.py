class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles > 0:
            numBottles %= numExchange
            ans += numBottles
        return ans
    



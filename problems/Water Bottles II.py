class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            newBottles = numBottles // numExchange
            ans += newBottles
            numBottles = newBottles + numBottles%numExchange
            numExchange += 1
        return ans
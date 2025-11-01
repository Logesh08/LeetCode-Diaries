from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > lowPrice:
                maxProfit = max(maxProfit, prices[i] - lowPrice)
            elif prices[i] < lowPrice:
                lowPrice = prices[i]
        return maxProfit
    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = 0
        smallestOnes = float("inf")
        smallestTwos = float("inf")


        for num in nums:
            if num % 3 == 1:
                smallestTwos = min(smallestTwos, num + smallestOnes)
                smallestOnes = min(smallestOnes, num)
            elif num % 3 == 2:
                smallestOnes = min(smallestOnes, num + smallestTwos)
                smallestTwos = min(smallestTwos, num)


            total += num

        if total % 3 == 0:
            return total
        if total % 3 == 1:
            return total - smallestOnes
        if total % 3 == 2:
            return total - smallestTwos
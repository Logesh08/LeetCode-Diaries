import heapq
from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
        
        while heap and len(heap) % k != 0:
            heapq.heappop(heap)

        return sum(heap)
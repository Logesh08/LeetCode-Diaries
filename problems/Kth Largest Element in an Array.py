import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        return minHeap[0]
    

# Slightly improvised version
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]
    

# Quick select
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k               # Translate to the k index from last, for largest

        def quickSelect(left: int, right: int) -> int:
            pivot = nums[right]    # To compare with each ones
            ptr = left             # moving pointer to compare

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[ptr] = nums[ptr], nums[i] # Swapping at ptr
                    ptr += 1

            nums[right], nums[ptr] = nums[ptr], nums[right]

            if ptr < k:
                return quickSelect(ptr + 1, right)
            elif ptr > k:
                return quickSelect(left, ptr - 1)
            else:
                return nums[ptr]
        
        return quickSelect(0, len(nums) - 1)
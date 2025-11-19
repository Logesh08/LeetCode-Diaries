# [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

Given an integer array <code>nums</code> and an integer <code>k</code>, return the <code>k^th</code> largest element in the array.

Note that it is the <code>k^th</code> largest element in the sorted order, not the <code>k^th</code> distinct element.

Can you solve it without sorting?

**Example 1:** 

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2:** 

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Constraints:** 

- <code>1 <= k <= nums.length <= 10^5</code>
- <code>-10^4 <= nums[i] <= 10^4</code>

---

## Solution

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        return minHeap[0]
```
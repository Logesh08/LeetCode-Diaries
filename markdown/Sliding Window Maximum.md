# [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

You are given an array of integers<code>nums</code>, there is a sliding window of size <code>k</code> which is moving from the very left of the array to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

**Example 1:** 

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       **3** 
 1 [3  -1  -3] 5  3  6  7       **3** 
 1  3 [-1  -3  5] 3  6  7      ** 5** 
 1  3  -1 [-3  5  3] 6  7       **5** 
 1  3  -1  -3 [5  3  6] 7       **6** 
 1  3  -1  -3  5 [3  6  7]      **7** 
```

**Example 2:** 

```
Input: nums = [1], k = 1
Output: [1]
```

**Constraints:** 

- <code>1 <= nums.length <= 10^5</code>
- <code>-10^4 <= nums[i] <= 10^4</code>
- <code>1 <= k <= nums.length</code>

---

## Solution
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []

        left = 0
        for right in range(len(nums)):
            while window and nums[window[-1]] <= nums[right]:
                window.pop()
            window.append(right)

            if left > window[0]:
                window.popleft()

            if (right + 1) >= k:
                res.append(nums[window[0]])
                left += 1

        return res
```
# [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=daily-question&envId=2025-08-24)

Given a binary array <code>nums</code>, you should delete one element from it.

Return the size of the longest non-empty subarray containing only <code>1</code>'s in the resulting array. Return <code>0</code> if there is no such subarray.

**Example 1:** 

```
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
```

**Example 2:** 

```
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
```

**Example 3:** 

```
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
```

**Constraints:** 

- <code>1 <= nums.length <= 10^5</code>
- <code>nums[i]</code> is either <code>0</code> or <code>1</code>.

---

### Solution in Python

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if all(nums):
            return(len(nums)-1)
        
        if sum(nums) == 0:
            return(0)

        leftSeen = False
        prevZero = left = -1
        singleZero = 0      # Only allowed case

        ans = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                if not leftSeen:
                    leftSeen = True
                    left = right
                ans = max(ans, right - left + 1 - singleZero)
            else:
                if not singleZero and leftSeen:
                    singleZero = 1
                elif leftSeen:
                    left = max(left, prevZero + 1)
                    singleZero = 1
                prevZero = right

        return ans
```
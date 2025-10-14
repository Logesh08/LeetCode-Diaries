# [3349. Adjacent Increasing Subarrays Detection I](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/description/?envType=daily-question&envId=2025-10-12)

Given an array <code>nums</code> of <code>n</code> integers and an integer <code>k</code>, determine whether there exist **two**  **adjacent**  <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r1n:" data-state="closed" class="">subarrays</button> of length <code>k</code> such that both subarrays are **strictly**  **increasing** . Specifically, check if there are **two**  subarrays starting at indices <code>a</code> and <code>b</code> (<code>a < b</code>), where:

- Both subarrays <code>nums[a..a + k - 1]</code> and <code>nums[b..b + k - 1]</code> are **strictly increasing** .
- The subarrays must be **adjacent** , meaning <code>b = a + k</code>.

Return <code>true</code> if it is possible to find **two ** such subarrays, and <code>false</code> otherwise.

**Example 1:** 

<div class="example-block">
Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3

Output: true

Explanation:

- The subarray starting at index <code>2</code> is <code>[7, 8, 9]</code>, which is strictly increasing.
- The subarray starting at index <code>5</code> is <code>[2, 3, 4]</code>, which is also strictly increasing.
- These two subarrays are adjacent, so the result is <code>true</code>.

**Example 2:** 

<div class="example-block">
Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5

Output: false

**Constraints:** 

- <code>2 <= nums.length <= 100</code>
- <code>1 < 2 * k <= nums.length</code>
- <code>-1000 <= nums[i] <= 1000</code>

---

## Solution

```python
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [1] * n

        for i in range(1,n):
            if nums[i] >nums[i - 1]:
                dp[i] += dp[i - 1]

        for window in range(n - 2 * k + 1):
            if dp[window + k - 1] >= k and dp[window + 2*k - 1] >= k:
                return True
        
        return False
```
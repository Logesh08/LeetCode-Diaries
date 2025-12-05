# [3432. Count Partitions with Even Sum Difference](https://leetcode.com/problems/count-partitions-with-even-sum-difference/?envType=daily-question&envId=2025-12-05)

You are given an integer array <code>nums</code> of length <code>n</code>.

A **partition**  is defined as an index <code>i</code> where <code>0 <= i < n - 1</code>, splitting the array into two **non-empty**  subarrays such that:

- Left subarray contains indices <code>[0, i]</code>.
- Right subarray contains indices <code>[i + 1, n - 1]</code>.

Return the number of **partitions**  where the **difference**  between the **sum**  of the left and right subarrays is **even** .

**Example 1:** 

<div class="example-block">
Input: nums = [10,10,3,7,6]

Output: 4

Explanation:

The 4 partitions are:

- <code>[10]</code>, <code>[10, 3, 7, 6]</code> with a sum difference of <code>10 - 26 = -16</code>, which is even.
- <code>[10, 10]</code>, <code>[3, 7, 6]</code> with a sum difference of <code>20 - 16 = 4</code>, which is even.
- <code>[10, 10, 3]</code>, <code>[7, 6]</code> with a sum difference of <code>23 - 13 = 10</code>, which is even.
- <code>[10, 10, 3, 7]</code>, <code>[6]</code> with a sum difference of <code>30 - 6 = 24</code>, which is even.

**Example 2:** 

<div class="example-block">
Input: nums = [1,2,2]

Output: 0

Explanation:

No partition results in an even sum difference.

**Example 3:** 

<div class="example-block">
Input: nums = [2,4,6,8]

Output: 3

Explanation:

All partitions result in an even sum difference.

**Constraints:** 

- <code>2 <= n == nums.length <= 100</code>
- <code>1 <= nums[i] <= 100</code>

---

## Solution

```python
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        partitions = 0
    
        right = sum(nums)
        left = 0
        for i in range(n - 1):
            left += nums[i]
            right -= nums[i]
            if (left - right) % 2 == 0:
                partitions += 1

        return partitions
```
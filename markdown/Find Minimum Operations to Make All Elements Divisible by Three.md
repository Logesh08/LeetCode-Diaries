# [3190. Find Minimum Operations to Make All Elements Divisible by Three](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/?envType=daily-question&envId=2025-11-21)

You are given an integer array <code>nums</code>. In one operation, you can add or subtract 1 from **any**  element of <code>nums</code>.

Return the **minimum**  number of operations to make all elements of <code>nums</code> divisible by 3.

**Example 1:** 

<div class="example-block">
Input: nums = [1,2,3,4]

Output: 3

Explanation:

All array elements can be made divisible by 3 using 3 operations:

- Subtract 1 from 1.
- Add 1 to 2.
- Subtract 1 from 4.

**Example 2:** 

<div class="example-block">
Input: nums = [3,6,9]

Output: 0

**Constraints:** 

- <code>1 <= nums.length <= 50</code>
- <code>1 <= nums[i] <= 50</code>

---

## Solution

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        minOperations = 0
        
        for num in nums:
            remaing = num % 3
            if remaing:
                minOperations += 1

        return minOperations
```
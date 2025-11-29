# [3512. Minimum Operations to Make Array Sum Divisible by K](https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/?envType=daily-question&envId=2025-11-28)

You are given an integer array <code>nums</code> and an integer <code>k</code>. You can perform the following operation any number of times:

- Select an index <code>i</code> and replace <code>nums[i]</code> with <code>nums[i] - 1</code>.

Return the **minimum**  number of operations required to make the sum of the array divisible by <code>k</code>.

**Example 1:** 

<div class="example-block">
Input: nums = [3,9,7], k = 5

Output: 4

Explanation:

- Perform 4 operations on <code>nums[1] = 9</code>. Now, <code>nums = [3, 5, 7]</code>.
- The sum is 15, which is divisible by 5.

**Example 2:** 

<div class="example-block">
Input: nums = [4,1,3], k = 4

Output: 0

Explanation:

- The sum is 8, which is already divisible by 4. Hence, no operations are needed.

**Example 3:** 

<div class="example-block">
Input: nums = [3,2], k = 6

Output: 5

Explanation:

- Perform 3 operations on <code>nums[0] = 3</code> and 2 operations on <code>nums[1] = 2</code>. Now, <code>nums = [0, 0]</code>.
- The sum is 0, which is divisible by 6.

**Constraints:** 

- <code>1 <= nums.length <= 1000</code>
- <code>1 <= nums[i] <= 1000</code>
- <code>1 <= k <= 100</code>

---

## Solution

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = 0

        for num in nums:
            total += num

        return total % k
```
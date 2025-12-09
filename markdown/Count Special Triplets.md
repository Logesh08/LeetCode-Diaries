# [3583. Count Special Triplets](https://leetcode.com/problems/count-special-triplets/description/?envType=daily-question&envId=2025-12-09)

You are given an integer array <code>nums</code>.

A **special triplet**  is defined as a triplet of indices <code>(i, j, k)</code> such that:

- <code>0 <= i < j < k < n</code>, where <code>n = nums.length</code>
- <code>nums[i] == nums[j] * 2</code>
- <code>nums[k] == nums[j] * 2</code>

Return the total number of **special triplets**  in the array.

Since the answer may be large, return it **modulo**  <code>10^9 + 7</code>.

**Example 1:** 

<div class="example-block">
Input: nums = [6,3,6]

Output: 1

Explanation:

The only special triplet is <code>(i, j, k) = (0, 1, 2)</code>, where:

- <code>nums[0] = 6</code>, <code>nums[1] = 3</code>, <code>nums[2] = 6</code>
- <code>nums[0] = nums[1] * 2 = 3 * 2 = 6</code>
- <code>nums[2] = nums[1] * 2 = 3 * 2 = 6</code>

**Example 2:** 

<div class="example-block">
Input: nums = [0,1,0,0]

Output: 1

Explanation:

The only special triplet is <code>(i, j, k) = (0, 2, 3)</code>, where:

- <code>nums[0] = 0</code>, <code>nums[2] = 0</code>, <code>nums[3] = 0</code>
- <code>nums[0] = nums[2] * 2 = 0 * 2 = 0</code>
- <code>nums[3] = nums[2] * 2 = 0 * 2 = 0</code>

**Example 3:** 

<div class="example-block">
Input: nums = [8,4,2,8,4]

Output: 2

Explanation:

There are exactly two special triplets:

- <code>(i, j, k) = (0, 1, 3)</code>

- <code>nums[0] = 8</code>, <code>nums[1] = 4</code>, <code>nums[3] = 8</code>
- <code>nums[0] = nums[1] * 2 = 4 * 2 = 8</code>
- <code>nums[3] = nums[1] * 2 = 4 * 2 = 8</code>

- <code>(i, j, k) = (1, 2, 4)</code>

- <code>nums[1] = 4</code>, <code>nums[2] = 2</code>, <code>nums[4] = 4</code>
- <code>nums[1] = nums[2] * 2 = 2 * 2 = 4</code>
- <code>nums[4] = nums[2] * 2 = 2 * 2 = 4</code>

**Constraints:** 

- <code>3 <= n == nums.length <= 10^5</code>
- <code>0 <= nums[i] <= 10^5</code>

---

## Solution

```python
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        right = defaultdict(int)
        left = defaultdict(int)
        res = 0

        for num in nums:
            right[num] += 1
        
        for num in nums:
            right[num] -= 1

            cur = num * 2
            if right[cur] and left[cur]:
                res += right[cur] * left[cur]

            left[num] += 1

        return res % MOD
```
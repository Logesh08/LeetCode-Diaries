# [3346. Maximum Frequency of an Element After Performing Operations I](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/description/?envType=daily-question&envId=2025-10-19)

You are given an integer array <code>nums</code> and two integers <code>k</code> and <code>numOperations</code>.

You must perform an **operation**  <code>numOperations</code> times on <code>nums</code>, where in each operation you:

- Select an index <code>i</code> that was **not**  selected in any previous operations.
- Add an integer in the range <code>[-k, k]</code> to <code>nums[i]</code>.

Return the **maximum**  possible <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r1n:" data-state="closed" class="">frequency</button> of any element in <code>nums</code> after performing the **operations** .

**Example 1:** 

<div class="example-block">
Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

- Adding 0 to <code>nums[1]</code>. <code>nums</code> becomes <code>[1, 4, 5]</code>.
- Adding -1 to <code>nums[2]</code>. <code>nums</code> becomes <code>[1, 4, 4]</code>.

**Example 2:** 

<div class="example-block">
Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

- Adding 0 to <code>nums[1]</code>.

**Constraints:** 

- <code>1 <= nums.length <= 10^5</code>
- <code>1 <= nums[i] <= 10^5</code>
- <code>0 <= k <= 10^5</code>
- <code>0 <= numOperations <= nums.length</code>

---

## Solution:

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxNum = max(nums)
        minNum = min(nums)

        freq = [0] * (maxNum + 1)
        pref = [0] * (maxNum + 1)

        for num in nums:
            freq[num] += 1
        for i in range(1, maxNum+1):
            pref[i] = pref[i - 1] + freq[i]

        ans = 1

        for i in range(minNum, maxNum+1):
            left = max(i - k - 1, 0)
            right = min(i + k, maxNum)
            total = min(pref[right] - pref[left], freq[i] + numOperations)
            if total > ans:
                ans = total

        return ans
```
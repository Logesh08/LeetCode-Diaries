# [3318. Find X-Sum of All K-Long Subarrays I](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/?envType=daily-question&envId=2025-11-02)

You are given an array <code>nums</code> of <code>n</code> integers and two integers <code>k</code> and <code>x</code>.

The **x-sum**  of an array is calculated by the following procedure:

- Count the occurrences of all elements in the array.
- Keep only the occurrences of the top <code>x</code> most frequent elements. If two elements have the same number of occurrences, the element with the **bigger**  value is considered more frequent.
- Calculate the sum of the resulting array.

**Note**  that if an array has less than <code>x</code> distinct elements, its **x-sum**  is the sum of the array.

Return an integer array <code>answer</code> of length <code>n - k + 1</code> where <code>answer[i]</code> is the **x-sum**  of the <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r1k:" data-state="closed" class="">subarray</button> <code>nums[i..i + k - 1]</code>.

**Example 1:** 

<div class="example-block">
Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

- For subarray <code>[1, 1, 2, 2, 3, 4]</code>, only elements 1 and 2 will be kept in the resulting array. Hence, <code>answer[0] = 1 + 1 + 2 + 2</code>.
- For subarray <code>[1, 2, 2, 3, 4, 2]</code>, only elements 2 and 4 will be kept in the resulting array. Hence, <code>answer[1] = 2 + 2 + 2 + 4</code>. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
- For subarray <code>[2, 2, 3, 4, 2, 3]</code>, only elements 2 and 3 are kept in the resulting array. Hence, <code>answer[2] = 2 + 2 + 2 + 3 + 3</code>.

**Example 2:** 

<div class="example-block">
Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]

Explanation:

Since <code>k == x</code>, <code>answer[i]</code> is equal to the sum of the subarray <code>nums[i..i + k - 1]</code>.

**Constraints:** 

- <code>1 <= n == nums.length <= 50</code>
- <code>1 <= nums[i] <= 50</code>
- <code>1 <= x <= k <= nums.length</code>

---

## Solution

```python
class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            window = nums[i:i + k]
            freq = Counter(window)
            sorted_freq = sorted(freq.items(), key=lambda a: (-a[1], -a[0]))
            top_x = set(num for num, _ in sorted_freq[:x])
            x_sum = sum(num for num in window if num in top_x)
            result.append(x_sum)

        return result
```
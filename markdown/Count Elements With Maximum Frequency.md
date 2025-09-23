# [3005. Count Elements With Maximum Frequency](https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2025-09-22)

You are given an array <code>nums</code> consisting of **positive**  integers.

Return the **total frequencies**  of elements in <code>nums</code>such that those elements all have the **maximum**  frequency.

The **frequency**  of an element is the number of occurrences of that element in the array.

**Example 1:** 

```
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
```

**Example 2:** 

```
Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
```

**Constraints:** 

- <code>1 <= nums.length <= 100</code>
- <code>1 <= nums[i] <= 100</code>

---

## Solution

```python
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        heiestFreq = -1
        ans = 0

        for num in nums:
            freq[num] += 1
            heiestFreq = max(heiestFreq, freq[num])

        for val in freq.values():
            if val == heiestFreq:
                ans += val

        return ans
```
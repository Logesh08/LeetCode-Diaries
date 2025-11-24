# [1018. Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5/description/?envType=daily-question&envId=2025-11-23)

You are given a binary array <code>nums</code> (**0-indexed** ).

We define <code>x<sub>i</sub></code> as the number whose binary representation is the subarray <code>nums[0..i]</code> (from most-significant-bit to least-significant-bit).

- For example, if <code>nums = [1,0,1]</code>, then <code>x<sub>0</sub> = 1</code>, <code>x<sub>1</sub> = 2</code>, and <code>x<sub>2</sub> = 5</code>.

Return an array of booleans <code>answer</code> where <code>answer[i]</code> is <code>true</code> if <code>x<sub>i</sub></code> is divisible by <code>5</code>.

**Example 1:** 

```
Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
```

**Example 2:** 

```
Input: nums = [1,1,1]
Output: [false,false,false]
```

**Constraints:** 

- <code>1 <= nums.length <= 10^5</code>
- <code>nums[i]</code> is either <code>0</code> or <code>1</code>.

---

## Solution

```python
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []

        cur = 0
        for n in nums:
            cur = ((cur << 1) + n) % 5
            res.append(cur % 5 == 0)

        return res
```
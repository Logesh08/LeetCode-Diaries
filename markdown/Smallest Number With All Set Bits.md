# [3370. Smallest Number With All Set Bits](https://leetcode.com/problems/smallest-number-with-all-set-bits/description/?envType=daily-question&envId=2025-10-27)

You are given a positive number <code>n</code>.

Return the **smallest**  number <code>x</code> **greater than**  or **equal to**  <code>n</code>, such that the binary representation of <code>x</code> contains only <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r0:" data-state="closed" class="">set bits</button>

**Example 1:** 

<div class="example-block">
Input: n = 5

Output: 7

Explanation:

The binary representation of 7 is <code>"111"</code>.

**Example 2:** 

<div class="example-block">
Input: n = 10

Output: 15

Explanation:

The binary representation of 15 is <code>"1111"</code>.

**Example 3:** 

<div class="example-block">
Input: n = 3

Output: 3

Explanation:

The binary representation of 3 is <code>"11"</code>.

**Constraints:** 

- <code>1 <= n <= 1000</code>

---

## Solution

```python
class Solution:
    def smallestNumber(self, n: int) -> int:
        binOfN = bin(n)[2:]
        return int("1" * len(binOfN), 2)
```
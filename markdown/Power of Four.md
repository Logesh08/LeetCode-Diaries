# [342. Power of Four](https://leetcode.com/problems/power-of-four/description/?envType=daily-question&envId=2025-08-15)

Given an integer <code>n</code>, return <code>true</code> if it is a power of four. Otherwise, return <code>false</code>.

An integer <code>n</code> is a power of four, if there exists an integer <code>x</code> such that <code>n == 4^x</code>.

**Example 1:** 

```
Input: n = 16
Output: true
```

**Example 2:** 

```
Input: n = 5
Output: false
```

**Example 3:** 

```
Input: n = 1
Output: true
```

**Constraints:** 

- <code>-2^31 <= n <= 2^31 - 1</code>

**Follow up:**  Could you solve it without loops/recursion?

---

## Solution

```python
def isPowerOfFour(n: int) -> bool:
    if n <= 0:
        return False
    # Check if n is a power of 2 and if the position of the only set bit is even
    return (n & (n - 1)) == 0 and (n - 1) % 3 == 0
```

```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n % 4 == 0:
            n //= 4

        return n == 1
```
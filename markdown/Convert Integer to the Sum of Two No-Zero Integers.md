# [1317. Convert Integer to the Sum of Two No-Zero Integers](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/submissions/?envType=daily-question&envId=2025-09-08)

**No-Zero integer**  is a positive integer that **does not contain any <code>0</code>**  in its decimal representation.

Given an integer <code>n</code>, return a list of two integers <code>[a, b]</code> where:

- <code>a</code> and <code>b</code> are **No-Zero integers** .
- <code>a + b = n</code>

The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

**Example 1:** 

```
Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
```

**Example 2:** 

```
Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.
```

**Constraints:** 

- <code>2 <= n <= 10^4</code>

---

## Solution

```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n+1):
            a = str(i)
            b = str(n - i)
            if "0" in a or "0" in b:
                continue
            return [i, n-i]
        return []
```
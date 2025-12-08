# [1925. Count Square Sum Triples](https://leetcode.com/problems/count-square-sum-triples/description/?envType=daily-question&envId=2025-12-08)

A **square triple**  <code>(a,b,c)</code> is a triple where <code>a</code>, <code>b</code>, and <code>c</code> are **integers**  and <code>a^2 + b^2 = c^2</code>.

Given an integer <code>n</code>, return the number of **square triples**  such that <code>1 <= a, b, c <= n</code>.

**Example 1:** 

```
Input: n = 5
Output: 2
Explanation
: The square triples are (3,4,5) and (4,3,5).
```

**Example 2:** 

```
Input: n = 10
Output: 4
Explanation
: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
```

**Constraints:** 

- <code>1 <= n <= 250</code>

---

## Solution

```python
class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for u in range(2, int(sqrt(n)) + 1):
            for v in range(1, u):
                if (u - v) & 1 == 0 or gcd(u, v) != 1:
                    continue                    
                c = u * u + v * v
                if c > n:
                    continue
                res += 2 * (n // c)
        return res
```
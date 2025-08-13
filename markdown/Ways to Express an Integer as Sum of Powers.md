# [2787. Ways to Express an Integer as Sum of Powers](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/?envType=daily-question&envId=2025-08-12)

Given two **positive**  integers <code>n</code> and <code>x</code>.

Return the number of ways <code>n</code> can be expressed as the sum of the <code>x^th</code> power of **unique**  positive integers, in other words, the number of sets of unique integers <code>[n<sub>1</sub>, n<sub>2</sub>, ..., n<sub>k</sub>]</code> where <code>n = n<sub>1</sub>^x + n<sub>2</sub>^x + ... + n<sub>k</sub>^x</code>.

Since the result can be very large, return it modulo <code>10^9 + 7</code>.

For example, if <code>n = 160</code> and <code>x = 3</code>, one way to express <code>n</code> is <code>n = 2^3 + 3^3 + 5^3</code>.

**Example 1:** 

```
Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 3^2 + 1^2 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2^nd power of unique integers.
```

**Example 2:** 

```
Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 4^1 = 4.
- n = 3^1 + 1^1 = 4.
```

**Constraints:** 

- <code>1 <= n <= 300</code>
- <code>1 <= x <= 5</code>

---

## Solution

```python
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MODULO = 10**9 + 7

        pows = []
        i = 1
        while i ** x <= n:
            pows.append(i ** x)
            i += 1

        print(pows)
        dp = [0] * (n+1)
        dp[0] = 1
        print(dp)

        for p in pows:
            for s in range(n,p-1,-1):
                dp[s] = (dp[s] + dp[s-p])
                print(dp)

        return dp[n] % MODULO
```
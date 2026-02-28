# [1680. Concatenation of Consecutive Binary Numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/?envType=daily-question&envId=2026-02-28)

Given an integer <code>n</code>, return the **decimal value**  of the binary string formed by concatenating the binary representations of <code>1</code> to <code>n</code> in order, **modulo ** <code>10^9 + 7</code>.

**Example 1:** 

```
Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 
```

**Example 2:** 

```
Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
```

**Example 3:** 

```
Input: n = 12
Output: 505379714
Explanation
: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 10^9 + 7, the result is 505379714.
```

**Constraints:** 

- <code>1 <= n <= 10^5</code>

---

## Solution

```python
def concatenatedBinary(n: int) -> int:
    mod = 10**9 + 7
    result = 0
    for i in range(1, n + 1):
        result = ((result << i.bit_length()) | i) % mod
    return result
```
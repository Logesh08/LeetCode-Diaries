# [1513. Number of Substrings With Only 1s](https://leetcode.com/problems/number-of-substrings-with-only-1s/description/?envType=daily-question&envId=2025-11-14)

Given a binary string <code>s</code>, return the number of substrings with all characters <code>1</code>'s. Since the answer may be too large, return it modulo <code>10^9 + 7</code>.

**Example 1:** 

```
Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.```

**Example 2:** 

```
Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
```

**Example 3:** 

```
Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
```

**Constraints:** 

- <code>1 <= s.length <= 10^5</code>
- <code>s[i]</code> is either <code>'0'</code> or <code>'1'</code>.

---

## Solution

```python
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        seqOnes = 0

        for c in s:
            if c == "1":
                seqOnes += 1
                res += seqOnes
            else:
                seqOnes = 0

        return res % MOD
```
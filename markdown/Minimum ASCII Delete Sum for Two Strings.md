# [712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/?envType=daily-question&envId=2026-01-10)

Given two strings <code>s1</code> and<code>s2</code>, return the lowest **ASCII**  sum of deleted characters to make two strings equal.

**Example 1:** 

```
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
```

**Example 2:** 

```
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
```

**Constraints:** 

- <code>1 <= s1.length, s2.length <= 1000</code>
- <code>s1</code> and <code>s2</code> consist of lowercase English letters.

---

## Solution

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        # dp[i][j] = min delete sum to make s1[i:] and s2[j:] equal
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: s2 is empty, delete all remaining chars from s1
        for i in range(m - 1, -1, -1):
            dp[i][n] = dp[i + 1][n] + ord(s1[i])
        
        # Base case: s1 is empty, delete all remaining chars from s2
        for j in range(n - 1, -1, -1):
            dp[m][j] = dp[m][j + 1] + ord(s2[j])
        
        # Fill the table from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        ord(s1[i]) + dp[i + 1][j],   # delete from s1
                        ord(s2[j]) + dp[i][j + 1]    # delete from s2
                    )
        
        return dp[0][0]
```
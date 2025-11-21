# [1930. Unique Length-3 Palindromic Subsequences](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2025-11-20)

Given a string <code>s</code>, return the number of **unique palindromes of length three**  that are a **subsequence**  of <code>s</code>.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted **once** .

A **palindrome**  is a string that reads the same forwards and backwards.

A **subsequence**  of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, <code>"ace"</code> is a subsequence of <code>"abcde"</code>.

**Example 1:** 

```
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
```

**Example 2:** 

```
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
```

**Example 3:** 

```
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
```

**Constraints:** 

- <code>3 <= s.length <= 10^5</code>
- <code>s</code> consists of only lowercase English letters.

---

## Solution

```python
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = {s[0]}
        right = {}

        for i in range(1, len(s)):
            right[s[i]] = right.get(s[i], 0) + 1

        res = set()

        for i in range(len(s)):
            right[s[i]] += 1
            for c in left:
                if right.get(c, 0) > 0:
                    res.add((c, s[i]))
            left.add(s[i])

        return len(res)
```
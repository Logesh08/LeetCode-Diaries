# [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/description/)

Given a string <code>s</code>, partition <code>s</code> such that every <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r1l:" data-state="closed" class="">substring</button> of the partition is a <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r1m:" data-state="closed" class="">**palindrome** </button>. Return all possible palindrome partitioning of <code>s</code>.

**Example 1:** 

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

**Example 2:** 

```
Input: s = "a"
Output: [["a"]]
```

**Constraints:** 

- <code>1 <= s.length <= 16</code>
- <code>s</code> contains only lowercase English letters.

---

## Solution

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        cur = []
        def dfs(start: int):
            if start == n:
                res.append(cur.copy())
                return
            
            for end in range(start, n):
                if isPalindrome(start, end):
                    cur.append(s[start:end + 1])
                    dfs(end + 1)
                    cur.pop()

        dfs(0)
        return res
```
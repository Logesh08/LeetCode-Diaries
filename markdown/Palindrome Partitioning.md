

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
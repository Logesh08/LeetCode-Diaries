# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)

Given <code>n</code> pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example 1:** 

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:** 

```
Input: n = 1
Output: ["()"]
```

**Constraints:** 

- <code>1 <= n <= 8</code>

---

## Solution

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openCount, closeCount, sol: List):
            if openCount == n and closeCount == n:
                res.append("".join(sol))
                return

            if openCount < n:
                sol.append("(")
                dfs(openCount+1,closeCount,sol)
                sol.pop()
            if closeCount < openCount:
                sol.append(")")
                dfs(openCount,closeCount+1,sol)
                sol.pop()

        dfs(0,0,[])

        return res
```
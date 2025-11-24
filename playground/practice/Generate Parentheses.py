from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        path = []
        def dfs(openCount: int, closeCount: int) -> None:
            if openCount == n and closeCount == n:
                res.append(''.join(path.copy()))
                return

            if openCount < n:
                path.append('(')
                dfs(openCount + 1, closeCount)
                path.pop()
            if closeCount < openCount:
                path.append(')')
                dfs(openCount, closeCount + 1)
                path.pop()

        dfs(0, 0)
        return res
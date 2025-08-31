from typing import List


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
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        cur: List[int] = []
        def dfs(i: int, total: int):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, total + candidates[i])
            cur.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res
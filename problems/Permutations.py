from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        visited = [False] * n
        path = []
        def dfs():
            if len(path) == n:
                res.append(path.copy())
                return

            for idx in range(n):
                if not visited[idx]:
                    path.append(nums[idx])
                    visited[idx] = True
                    dfs()
                    path.pop()
                    visited[idx] = False

        dfs()
        return res
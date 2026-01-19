from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjs = [[] for _ in range(n)]

        for u, v in edges:
            adjs[u].append(v)
            adjs[v].append(u)

        res = 0

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for nei in adjs[node]:
                if nei == prev:
                    continue
                dfs(nei, node)
            return True

        for i in range(n):
            if dfs(i, -1):
                res += 1

        return res
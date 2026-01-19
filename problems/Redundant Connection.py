from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node):
            p = parents[node]
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            



###

# This is for first repeat detection not ideal for last one detection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        adjs = defaultdict(list)

        for u, v in edges:
            adjs[u].append(v)
            adjs[v].append(u)

        res = [[]]

        def dfs(node, prev):
            if node in visited:
                res[0] = [node, prev]
                return
            visited.add(node)
            for nei in adjs[node]:
                if nei == prev:
                    continue
                dfs(nei, node)
            return

        dfs(1, -1)
        return res[0]
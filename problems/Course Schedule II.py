from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashMap = {i : [] for i in range(numCourses)}

        for crs, preq in prerequisites:
            hashMap[crs].append(preq)

        res = []
        visited = set()
        cycle = set()

        def dfs(crs: int) -> None:
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for preq in hashMap[crs]:
                if not dfs(preq):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
            
        return res
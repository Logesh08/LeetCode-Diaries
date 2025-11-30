from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap = {i : [] for i in range(numCourses)}

        for crs, preq in prerequisites:
            hashMap[crs].append(preq)

        visiting = set()
        def dfs(crs: int) -> None:
            if crs in visiting:
                return False
            if not hashMap[crs]:
                return True
            
            visiting.add(crs)
            for preq in hashMap[crs]:
                if not dfs(preq):
                    return False
            visiting.remove(crs)
            
            hashMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False

        return True
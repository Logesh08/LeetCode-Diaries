import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        if n < 3 or m < 3:
            return 0


        visited = [[False] * m for _ in range(n)]
        heap = []

        def push(i, j, level):
            if not visited[i][j]:
                visited[i][j] = True
                heapq.heappush(heap, (level, i, j))

        # seed all borders
        for i in range(n):
            push(i, 0, heightMap[i][0])
            push(i, m - 1, heightMap[i][m - 1])
        for j in range(m):
            push(0, j, heightMap[0][j])
            push(n - 1, j, heightMap[n - 1][j])

        ans = 0
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            level, r, c = heapq.heappop(heap)
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    nh = heightMap[nr][nc]
                    if nh < level:
                        ans += level - nh
                        push(nr, nc, level)  # water fills up to current rim
                    else:
                        push(nr, nc, nh)     # higher ground becomes new rim

        return ans





# WONT WORK

from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        if n < 3 or m < 3:
            return 0
        
        ans = 0

        waterLevel = [[float('inf')]* m for _ in range(n)]

        for i in range(n):
            waterLevel[i][0] = heightMap[i][0]
            waterLevel[i][-1] = heightMap[i][-1]
        for j in range(m):
            waterLevel[0][j] = heightMap[0][j]
            waterLevel[-1][j] = heightMap[-1][j]

        
        
        print(waterLevel)

        for i in range(1, n-1, 1):
            for j in range(1, m-1, 1):
                if waterLevel[i][j] > heightMap[i][j]:
                    ans += waterLevel[i][j] - heightMap[i][j]

        return ans
    

sol1 = Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])
sol2 = Solution().trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]])
print(sol1)
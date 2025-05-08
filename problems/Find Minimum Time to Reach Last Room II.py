from typing import List
import math
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        n,m = len(moveTime), len(moveTime[0])
        shortesTime = [[[math.inf, math.inf] for _ in range(m)] for _ in range(n)]
        visited = set()
        directions = [[0,1],[-1,0],[1,0],[0,-1]]

        shortesTime[0][0][0] = 0
        heap = [(0,0,0,False)]

        while heap:
            
            time,x,y,flip = heapq.heappop(heap)

            if time > shortesTime[x][y][flip]:
                continue
            
            if x == n-1 and y == m-1:
                return time

            for dx,dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    step_cost    = 1 if flip==0 else 2
                    new_parity   = 1 - flip
                    newTime = max(moveTime[nx][ny],time) + step_cost

                    if shortesTime[nx][ny][new_parity] > newTime: 
                        shortesTime[nx][ny][new_parity] = newTime
                        heapq.heappush(heap,(newTime,nx,ny,new_parity))


        return -1
    

    

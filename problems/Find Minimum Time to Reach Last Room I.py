# LeetCode Problem 3341: Find Minimum Time to Reach Last Room I
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/



# There is a dungeon with n x m rooms arranged as a grid.

# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

# Return the minimum time to reach the room (n - 1, m - 1).

# Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

# Example 1:

# Input: moveTime = [[0,4],[4,4]]

# Output: 6

# Explanation:

# The minimum time required is 6 seconds.

# At time t == 4, move from room (0, 0) to room (1, 0) in one second.
# At time t == 5, move from room (1, 0) to room (1, 1) in one second.
# Example 2:

# Input: moveTime = [[0,0,0],[0,0,0]]

# Output: 3

# Explanation:

# The minimum time required is 3 seconds.

# At time t == 0, move from room (0, 0) to room (1, 0) in one second.
# At time t == 1, move from room (1, 0) to room (1, 1) in one second.
# At time t == 2, move from room (1, 1) to room (1, 2) in one second.
# Example 3:

# Input: moveTime = [[0,1],[1,2]]

# Output: 3

 

# Constraints:

# 2 <= n == moveTime.length <= 50
# 2 <= m == moveTime[i].length <= 50
# 0 <= moveTime[i][j] <= 109



import heapq
from typing import List
import math



# Clasic approach using Dijkstra's algorithm
# This is the first time I am using Dijkstra's algorithm in LeetCode
# But I definitely remember using the four directional List in the past

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        n,m = len(moveTime) , len(moveTime[0])
        shortestTime = [[math.inf]*m for _ in range(n)]
        visited = set()

        shortestTime[0][0] = 0
        heap = [(0,0,0)]

        while heap:
            time, x, y = heapq.heappop(heap)

            if (x,y) in visited:
                continue

            visited.add((x,y))

            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            for dx,dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    newTime = max(moveTime[nx][ny],shortestTime[x][y]) + 1

                    if shortestTime[nx][ny] > newTime:
                        shortestTime[nx][ny] = newTime
                        heapq.heappush(heap,(newTime,nx,ny))

        
        return shortestTime[n-1][m-1]
    







# Much optimized version without using visited and early exit


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        n,m = len(moveTime) , len(moveTime[0])
        shortestTime = [[math.inf]*m for _ in range(n)]

        shortestTime[0][0] = 0
        heap = [(0,0,0)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while heap:
            time, x, y = heapq.heappop(heap)

            if time > shortestTime[x][y]:
                continue

            if x == n-1 and y == m-1:
                return time



            for dx,dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    newTime = max(moveTime[nx][ny],shortestTime[x][y]) + 1

                    if shortestTime[nx][ny] > newTime:
                        shortestTime[nx][ny] = newTime
                        heapq.heappush(heap,(newTime,nx,ny))

        
        return -1
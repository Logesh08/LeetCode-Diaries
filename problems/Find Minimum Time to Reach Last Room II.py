# LeetCode Problem 3342: Find Minimum Time to Reach Last Room II
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/



# There is a dungeon with n x m rooms arranged as a grid.

# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

# Return the minimum time to reach the room (n - 1, m - 1).

# Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

# Example 1:

# Input: moveTime = [[0,4],[4,4]]

# Output: 7

# Explanation:

# The minimum time required is 7 seconds.

# At time t == 4, move from room (0, 0) to room (1, 0) in one second.
# At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.
# Example 2:

# Input: moveTime = [[0,0,0,0],[0,0,0,0]]

# Output: 6

# Explanation:

# The minimum time required is 6 seconds.

# At time t == 0, move from room (0, 0) to room (1, 0) in one second.
# At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
# At time t == 3, move from room (1, 1) to room (1, 2) in one second.
# At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.
# Example 3:

# Input: moveTime = [[0,1],[1,2]]

# Output: 4

 

# Constraints:

# 2 <= n == moveTime.length <= 750
# 2 <= m == moveTime[i].length <= 750
# 0 <= moveTime[i][j] <= 10^9











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
    

    

## Much simpler and practical
# Could have easily foun cost like this

class Solution:
    def minTimeToReach(self, moveTime):
        n = len(moveTime)
        m = len(moveTime[0])
        INF = float('inf')
        dp = [[INF]*m for _ in range(n)]
        minh = [(0, 0, 0)]
        moveTime[0][0] = 0

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while minh:
            currTime, currRow, currCol = heapq.heappop(minh)
            if currTime >= dp[currRow][currCol]:
                continue
            if currRow == n - 1 and currCol == m - 1:
                return currTime
            dp[currRow][currCol] = currTime

            for dr, dc in directions:
                nextRow = currRow + dr
                nextCol = currCol + dc
                if 0 <= nextRow < n and 0 <= nextCol < m and dp[nextRow][nextCol] == INF:
                    cost  = (currRow + currCol) % 2 + 1
                    start = max(moveTime[nextRow][nextCol], currTime)
                    nextTime = start + cost
                    heapq.heappush(minh, (nextTime, nextRow, nextCol))

        return -1
    


# Beats 80% + 


class Solution(object):
    def minTimeToReach(self, moveTime):
        n = len(moveTime)
        m = len(moveTime[0])
        minh = [(0, 0, 0, 1)]
        heapq.heapify(minh)
        minTime = set((0, 0))  
        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        while minh :
            currTime, x, y, i  = heapq.heappop(minh)
            if x == n - 1 and y == m - 1 :
                return currTime
            for dx,dy in direction :
                nx,ny  = x + dx , y + dy
                if 0<= nx < n and 0<= ny < m and (nx,ny) not in minTime :
                    
                    next_time = max(currTime, moveTime[nx][ny]) + i
                    heapq.heappush(minh, (next_time, nx, ny, 3 - i))
                    minTime.add((nx, ny))
        return -1
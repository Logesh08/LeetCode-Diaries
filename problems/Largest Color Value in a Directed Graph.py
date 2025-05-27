# LeetCode Problem 1857: Largest Color Value in a Directed Graph
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/


# There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

# You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

# Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

 

# Example 1:



# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
# Example 2:



# Input: colors = "a", edges = [[0,0]]
# Output: -1
# Explanation: There is a cycle from 0 to 0.
 

# Constraints:

# n == colors.length
# m == edges.length
# 1 <= n <= 10^5
# 0 <= m <= 10^5
# colors consists of lowercase English letters.
# 0 <= aj, bj < n




class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque
        
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        
        # Build the graph and indegree array
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Topological sort using Kahn's algorithm
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        color_count = [[0] * 26 for _ in range(n)]
        max_color_value = 0
        
        while queue:
            node = queue.popleft()
            color_index = ord(colors[node]) - ord('a')
            color_count[node][color_index] += 1
            
            # Update the maximum color value
            max_color_value = max(max_color_value, color_count[node][color_index])
            
            for neighbor in graph[node]:
                for c in range(26):
                    color_count[neighbor][c] = max(color_count[neighbor][c], color_count[node][c])
                
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If there are still nodes with non-zero indegree, there is a cycle
        if any(indegree[i] > 0 for i in range(n)):
            return -1
        
        return max_color_value
# LeetCode Problem 2359: Find Closest Node to Given Two Nodes
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/


# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

# You are also given two integers node1 and node2.

# Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

# Note that edges may contain cycles.

 

# Example 1:


# Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
# Output: 2
# Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
# The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
# Example 2:


# Input: edges = [1,2,-1], node1 = 0, node2 = 2
# Output: 2
# Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
# The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.
 

# Constraints:

# n == edges.length
# 2 <= n <= 10^5
# -1 <= edges[i] < n
# edges[i] != i
# 0 <= node1, node2 < n






class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start):
            dist = [-1] * len(edges)
            queue = deque([start])
            dist[start] = 0
            
            while queue:
                node = queue.popleft()
                next_node = edges[node]
                if next_node != -1 and dist[next_node] == -1:
                    dist[next_node] = dist[node] + 1
                    queue.append(next_node)
            return dist
        
        dist1 = bfs(node1)
        dist2 = bfs(node2)
        
        min_max_dist = float('inf')
        result_node = -1
        
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_max_dist or (max_dist == min_max_dist and i < result_node):
                    min_max_dist = max_dist
                    result_node = i
        
        return result_node
    



# Altrnate big brain approach

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        visited1 = set()
        visited2 = set()
        while node1 != -1 or node2 != -1:
            if node1 in visited1:
                node1 = -1
            if node2 in visited2:
                node2 = -1
            if node1 != -1:
                visited1.add(node1)
            if node2 != -1:
                visited2.add(node2)
            if node1 in visited2 and node2 in visited1:
                return min(node1, node2)
            if node1 in visited2:
                return node1
            if node2 in visited1:
                return node2
            if node1 != -1:
                node1 = edges[node1]
            if node2 != -1:
                node2 = edges[node2]       
        return -1
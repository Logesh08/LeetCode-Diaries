# [3650. Minimum Cost Path with Edge Reversals](https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/description/?envType=daily-question&envId=2026-01-27)

You are given a directed, weighted graph with <code>n</code> nodes labeled from 0 to <code>n - 1</code>, and an array <code>edges</code> where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code> represents a directed edge from node <code>u<sub>i</sub></code> to node <code>v<sub>i</sub></code> with cost <code>w<sub>i</sub></code>.

Each node <code>u<sub>i</sub></code> has a switch that can be used **at most once** : when you arrive at <code>u<sub>i</sub></code> and have not yet used its switch, you may activate it on one of its incoming edges <code>v<sub>i</sub> → u<sub>i</sub></code> reverse that edge to <code>u<sub>i</sub> → v<sub>i</sub></code> and **immediately**  traverse it.

The reversal is only valid for that single move, and using a reversed edge costs <code>2 * w<sub>i</sub></code>.

Return the **minimum**  total cost to travel from node 0 to node <code>n - 1</code>. If it is not possible, return -1.

**Example 1:** 

<div class="example-block">
Input: n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]

Output: 5

Explanation: 

**<img alt="" src="https://assets.leetcode.com/uploads/2025/05/07/e1drawio.png" style="width: 171px; height: 111px;">** 

- Use the path <code>0 → 1</code> (cost 3).
- At node 1 reverse the original edge <code>3 → 1</code> into <code>1 → 3</code> and traverse it at cost <code>2 * 1 = 2</code>.
- Total cost is <code>3 + 2 = 5</code>.

**Example 2:** 

<div class="example-block">
Input: n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]

Output: 3

Explanation:

- No reversal is needed. Take the path <code>0 → 2</code> (cost 1), then <code>2 → 1</code> (cost 1), then <code>1 → 3</code> (cost 1).
- Total cost is <code>1 + 1 + 1 = 3</code>.

**Constraints:** 

- <code>2 <= n <= 5 * 10^4</code>
- <code>1 <= edges.length <= 10^5</code>
- <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code>
- <code>0 <= u<sub>i</sub>, v<sub>i</sub> <= n - 1</code>
- <code>1 <= w<sub>i</sub> <= 1000</code>

---

## Solution

```python
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Building augmented graph
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))  # Reverse edge

        # Initialize distance array from 0 node
        dist = [math.inf] * n
        dist[0] = 0

        # Dijkstra
        heap = [(0, 0)]
        while heap:
            d, u = heapq.heappop(heap)
            if u == n - 1:  # Early exit
                return d
            if d != dist[u]:  # Stale edge
                continue
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:  # Edge relaxation
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))

        # No path found
        return -1
```
# Number of Connected Components in an Undirected Graph

**Difficulty:** Medium

## Problem Description

There is an undirected graph with `n` nodes. There is also an `edges` array, where `edges[i] = [a, b]` means that there is an edge between node `a` and node `b` in the graph.

The nodes are numbered from `0` to `n - 1`.

Return the total number of connected components in that graph.

---

## Examples

**Example 1:**

**Input:**
```
n = 3
edges = [[0,1], [0,2]]
```

**Output:**
```
1
```

**Example 2:**

**Input:**
```
n = 6
edges = [[0,1], [1,2], [2,3], [4,5]]
```

**Output:**
```
2
```

---

## Constraints

- `1 <= n <= 100`
- `0 <= edges.length <= n * (n - 1) / 2`

---

## Solutions

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjs = [[] for _ in range(n)]

        for u, v in edges:
            adjs[u].append(v)
            adjs[v].append(u)

        res = 0

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for nei in adjs[node]:
                if nei == prev:
                    continue
                dfs(nei, node)
            return True

        for i in range(n):
            if dfs(i, -1):
                res += 1

        return res
```
from collections import deque

def getMaxTime(g_nodes, g_from, g_to):
    # Build adjacency list
    adj = [[] for _ in range(g_nodes + 1)]
    for u, v in zip(g_from, g_to):
        adj[u].append(v)
        adj[v].append(u)

    def bfs(start):
        dist = [-1] * (g_nodes + 1)
        q = deque([start])
        dist[start] = 0
        farthest_node = start

        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
                    if dist[v] > dist[farthest_node]:
                        farthest_node = v

        return farthest_node, dist[farthest_node]

    # Edge case: single node
    if g_nodes <= 1:
        return 0

    # 1st BFS: find one endpoint of diameter
    a, _ = bfs(1)
    # 2nd BFS: distance from that endpoint = diameter
    b, diameter = bfs(a)

    return diameter

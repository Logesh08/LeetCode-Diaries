# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors: List[Node] = neighbors if neighbors is not None else []
from typing import List, Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashMap = {}

        def dfs(node: Node):
            if node in hashMap:
                return hashMap[node]
            
            newNode = Node(node.val)
            hashMap[node] = newNode
            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))

            return newNode

        return dfs(node) if node else None
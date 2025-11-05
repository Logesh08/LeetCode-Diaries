from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        originalNodes = {None: None}

        cur = head
        while cur:
            originalNodes[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            originalNodes[cur].next = originalNodes[cur.next]
            originalNodes[cur].random = originalNodes[cur.random]
            cur = cur.next

        return originalNodes[head]
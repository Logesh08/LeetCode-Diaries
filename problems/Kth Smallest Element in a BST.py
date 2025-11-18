# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
import heapq
from typing import Optional


# Space: O(2n)
# Time: O(n + k)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        queue = deque()
        queue.append(root)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    heapq.heappush(heap, node.val)
                    queue.append(node.left)
                    queue.append(node.right)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return heapq.heappop(heap)
    



# DSF
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k - 1]
import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        headRef = ListNode()
        cur = headRef

        while heap:
            v, i, node = heapq.heappop(heap)

            cur.next = node
            cur = cur.next

            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return headRef.next
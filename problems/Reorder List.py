from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = deque()
        while head:
            queue.append(head)
            head = head.next

        result = ListNode()
        head = result

        while queue:
            result.next = queue.popleft()
            result = result.next
            if queue:
                result.next = queue.pop()
                result = result.next

        result.next = None
        head = head.next

        return None





# Solution is invalid, cuz we cant return the ans, also 
# Memory wise we have restriction
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = deque()
        while head:
            queue.append(head)
            head = head

        result = ListNode()

        while queue:
            result = queue.popleft()
            if queue:
                result.next = queue.pop()
                result = result.next.next

        return result.next
    


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


## My Own hard worked, brain squeezed solution ahhhhHhhhhhh!!!!
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            if not next:
                break
            head = next
        return head
    

# Ahh, seems like i can return the prev itself!
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
    


# Recursive version
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def doReverse(cur: ListNode, prev: ListNode):
            if cur:
                next = cur.next
                cur.next = prev
                doReverse(next, cur)
            else:
                return prev # It's head, when we come here, we are past the tail
        return doReverse(head, None)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenOfList = 0
        dummyHead = head
        while dummyHead:
            lenOfList += 1
            dummyHead = dummyHead.next

        target = lenOfList - n
        if target == 0:
            return head.next

        curLen = 0
        dummyHead = head
        while dummyHead:
            curLen += 1
            if curLen == target:
                dummyHead.next = dummyHead.next.next
            dummyHead = dummyHead.next

        return head
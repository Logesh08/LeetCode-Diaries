from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        dummyNode = ListNode()
        dummyNode.next = head

        prevLastNode = dummyNode
        ctr = 1
        while head:
            nextNode = head.next
            if ctr == 1:
                curFirstNode = head
            elif ctr == k:
                nextStart = head.next
                tempPrev = curFirstNode
                tempCur = curFirstNode.next
                for _ in range(k-1):
                    tempNext = tempCur.next
                    tempCur.next = tempPrev
                    tempPrev = tempCur
                    tempCur = tempNext
                prevLastNode.next = head
                curFirstNode.next = nextStart
                prevLastNode = curFirstNode
                ctr = 0
            ctr += 1
            head = nextNode

        return dummyNode.next
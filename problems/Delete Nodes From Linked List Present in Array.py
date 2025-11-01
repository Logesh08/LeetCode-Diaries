# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        newHead = ListNode()
        headRef = newHead
        while head:
            if head.val not in nums:
                newHead.next = ListNode(head.val)
                newHead = newHead.next
            head = head.next
        return headRef.next
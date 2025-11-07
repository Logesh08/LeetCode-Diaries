from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val:int = val
        self.next:ListNode = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.mergeTwoList(list1, list2))
            lists = mergedLists

        return lists[0]
        
    def mergeTwoList(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoList(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoList(list1, list2.next)
            return list2
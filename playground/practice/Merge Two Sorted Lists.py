# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        listRef = mergedList

        while list1 and list2:
            if list1.val > list2.val:
                mergedList.next = list1
                list1 = list1.next
            else:
                mergedList.next = list2
                list2 = list2.next
            mergedList = mergedList.next

        if list1:
            mergedList = list1
        if list2:
            mergedList = list2

        return listRef.next
    



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
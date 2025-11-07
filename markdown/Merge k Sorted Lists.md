# [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)

You are given an array of <code>k</code> linked-lists <code>lists</code>, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Example 1:** 

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
```

**Example 2:** 

```
Input: lists = []
Output: []
```

**Example 3:** 

```
Input: lists = [[]]
Output: []
```

**Constraints:** 

- <code>k == lists.length</code>
- <code>0 <= k <= 10^4</code>
- <code>0 <= lists[i].length <= 500</code>
- <code>-10^4 <= lists[i][j] <= 10^4</code>
- <code>lists[i]</code> is sorted in **ascending order** .
- The sum of <code>lists[i].length</code> will not exceed <code>10^4</code>.

---

## Solution

```python
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
```
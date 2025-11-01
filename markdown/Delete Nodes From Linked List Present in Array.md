# [3217. Delete Nodes From Linked List Present in Array](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/?envType=daily-question&envId=2025-10-30)

You are given an array of integers <code>nums</code> and the <code>head</code> of a linked list. Return the <code>head</code> of the modified linked list after **removing**  all nodes from the linked list that have a value that exists in <code>nums</code>.

**Example 1:** 

<div class="example-block">
Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:

**<img alt="" src="https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample0.png" style="width: 400px; height: 66px;">** 

Remove the nodes with values 1, 2, and 3.

**Example 2:** 

<div class="example-block">
Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]

Explanation:

<img alt="" src="https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample1.png" style="height: 62px; width: 450px;">

Remove the nodes with value 1.

**Example 3:** 

<div class="example-block">
Input: nums = [5], head = [1,2,3,4]

Output: [1,2,3,4]

Explanation:

**<img alt="" src="https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample2.png" style="width: 400px; height: 83px;">** 

No node has value 5.

**Constraints:** 

- <code>1 <= nums.length <= 10^5</code>
- <code>1 <= nums[i] <= 10^5</code>
- All elements in <code>nums</code> are unique.
- The number of nodes in the given list is in the range <code>[1, 10^5]</code>.
- <code>1 <= Node.val <= 10^5</code>
- The input is generated such that there is at least one node in the linked list that has a value not present in <code>nums</code>.

---

## Solution

```python
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        newHead = ListNode()
        headRef = newHead
        while head:
            if head.val not in nums:
                newHead.next = head
                newHead = newHead.next
            head = head.next
            newHead.next = None # Removing nodes attached to tail, because we need to attach only those which are not in nums

        return headRef.next
```
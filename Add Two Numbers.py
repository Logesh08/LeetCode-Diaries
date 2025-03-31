# LeetCode Problem 2: Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
#
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contains a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
# imgUrl: https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# Explanation: 9999999 + 9999 = 10009998.
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        startingRef = ref = None
        carry = 0
        while l1 or l2 or carry:
            current = ListNode()
            newVal = 0
            if l1:
                newVal += l1.val
                l1 = l1.next
            if l2:
                newVal += l2.val
                l2 = l2.next
            
            newVal += carry
            if newVal>9:
                carry = newVal // 10
                newVal %= 10
            else:
                carry = 0
            
            current.val = newVal
            if not startingRef:
                ref = current
                startingRef = ref
            else:
                ref.next = current
                ref = current
        return startingRef


# Demn after a long time this program felt like a good warm up lol
# Seems like this is the second best solution


# Here is the best solution, seems the major difference is the amount of if else used is reduced
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:       
        cur = root=  ListNode()
        carry = 0
        while l1 or l2 or carry:
            sum0 = carry
            if l1:
                sum0 += l1.val
                l1 = l1.next
            if l2:
                sum0 += l2.val
                l2 = l2.next
            carry = sum0 // 10
         
            cur.next = ListNode(sum0 % 10)
            cur = cur.next
        return root.next
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        groups = 0

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()

            if num != 0 and (not stack or stack[-1] != num):
                groups += 1
                stack.append(num)

        return groups
            
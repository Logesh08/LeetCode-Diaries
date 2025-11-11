from typing import List

# 1min 38 secs
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(numbers):
            carry = target - num
            if carry in hashMap:
                return [hashMap[carry], i+1]
            hashMap[num] = i+1

        return []
    

# 2min 2secs
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            elif current > target:
                right -= 1
            else:
                left += 1

        return []
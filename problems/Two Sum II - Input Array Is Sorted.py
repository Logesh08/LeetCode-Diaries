from typing import List


# I derived this solution after realising the List is sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            cur = numbers[left] + numbers[right]
            if cur == target:
                return [left+1, right+1]
            if cur < target:
                left += 1
            else:
                right -= 1
        return []




# Failed attempt cuz its TLE prone...^~^
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            for j in range(i+1,n):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return []
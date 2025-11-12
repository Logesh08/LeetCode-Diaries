from typing import List

# 3min 53 secs
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            curHeight = min(height[left], height[right])
            width = right - left
            maxArea = max(curHeight * width, maxArea)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxArea
    
# Finally in a while I have solved a problem in my first try it feels so good!

# Cuz to other problesm in our 45 series I did made some minor mistakes, guess this time we are doing good.


# Lol i wish 3d rain water trapping is this simple!
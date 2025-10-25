from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                water += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                water += maxRight - height[right]

        return water









# Great solution but will get memory limit! #SKIP
class Solution:
    def trap(self, height: List[int]) -> int:
        r = max(height)
        c = len(height)
        mat = [[0]*c for _ in range(r)]
        ans = 0

        for j in range(c):
            ctr = r - 1
            for _ in range(height[j]):
                mat[ctr][j] = 1
                ctr -= 1

        # for row in mat:
        #     print(row)
        
        for j in range(c-1):
            base = r - 1
            while base >=0 and mat[base][j] == 1:
                left = j
                right = left + 1
                while right < c and mat[base][right] == 0:
                    right += 1
                if right != c:
                    ans += right - left - 1
                base -= 1

        # print(ans)
        return ans


Solution().trap([4,2,0,3,2,5])
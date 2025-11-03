from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [nums[0]]  # Initialising first element of list as max for first window
        prevMaxInd = 0
        nextMax = float("-inf")
        nextMaxInd = -1

        for i in range(1, k):
            if nums[i] >= res[-1]:
                prevMaxInd = i
                res[-1] = nums[i]

        left = 1
        for i in range(k, len(nums)):
            if prevMaxInd >= left and nums[i] >= res[-1]:
                res.append(nums[i])
                prevMaxInd = i
            else:
                # Case where the prevMax moves out of the window
                if nums[i] >= nextMax:
                    res.append(nums[i])
                    prevMaxInd = i
                else:
                    res.append(nextMax)
                    prevMaxInd = nextMaxInd

            if i > prevMaxInd and nums[i] >= nextMax:
                nextMax = nums[i]
                nextMaxInd = i
            else:
                nextMax = float("-inf")

            left += 1


        return res



print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
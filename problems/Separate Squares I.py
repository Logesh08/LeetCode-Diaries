from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        totalArea = 0.0
        minY = float("inf")
        maxY = float("-inf")

        for x, y, l in squares:
            totalArea += l * l
            minY = min(minY, y)
            maxY = max(maxY, y)

        target = totalArea / 2.0

        def findAreaAbove(h: int) -> float:
            area = 0.0
            for x, y, l in squares: 
                if y > h:
                    # these are fully available sqares
                    area += l * l
                elif y + l > h:
                    # these squares are being cut through
                    area += (y + l  - h) * l
                else:
                    # skip squares at bottom
                    pass
            return area
        
        low, high = minY, maxY
        tolernce = 1e-5


        while high - low > tolernce:
            mid = (low + high) / 2.0
            areaAbove = findAreaAbove(mid)
            if areaAbove == target:
                break
            elif areaAbove < target:
                mid = low
            else:
                mid = high

        return (low + high) / 2.0


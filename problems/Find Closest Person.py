class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xToZ = abs(z - x)
        yToZ = abs(z - y)
        if xToZ == yToZ:
            return 0
        elif xToZ > yToZ:
            return 2
        else:
            return 1
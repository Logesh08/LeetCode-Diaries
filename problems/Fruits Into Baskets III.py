from typing import List

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        size = 1
        while size < self.n: size <<= 1
        self.size = size
        self.tree = [float("-inf")] * (2*size)

        for index, value in enumerate(data):
            self.tree[size + index] = value

        for index in range(size-1,0,-1):
            self.tree[index] = max(self.tree[2*index],self.tree[2*index+1])

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[2*index],self.tree[2*index+1])

    # I actyually thought why always Iterate to the root? Absolutely not right
    # We need to check if there is change in the parent of the leaf else only
    # we need to traverse and update
    def updateWithSpeed(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            updatedValue = max(self.tree[2*index],self.tree[2*index+1])
            if self.tree[index] == updatedValue:
                break
            self.tree[index] = updatedValue


    def leftmostAtLeast(self, value):
        if self.tree[1] < value:
            return -1
        
        index = 1
        left, right = 0, self.size - 1
        
        while index < self.size:
            mid = (left + right) // 2
            if self.tree[2*index] >= value:
                index = 2*index
                right = mid
            else:
                index = 2*index + 1
                left = mid + 1

        pos = index - self.size
        return pos if pos < self.n else -1
    

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        placed = 0
        segmentTree = SegmentTree(baskets)
        for fruit in fruits:
            index = segmentTree.leftmostAtLeast(fruit)
            if index != -1:
                placed += 1
                segmentTree.updateWithSpeed(index, float('-inf'))
        return len(fruits) - placed
# Example of MAX-segment tree

class SegmentTree:
    # Here we construct the segment tree
    def __init__(self, data):
        self.n = len(data)
        size = 1
        while size < self.n: size <<= 1
        self.size = size
        self.tree = [float('-inf')] * (2*size)

        # Leaf values initialisation
        for index, value in enumerate(data):
            self.tree[size + index] = value

        # Leef to top till root initialisation
        for index in range(size-1,0,-1):
            self.tree[index] = max(self.tree[2*index],self.tree[2*index+1])

    def update(self, pos, value):
        index = self.size + pos
        self.tree[index] = value

        while index > 1:
            index //= 2
            updatedValue =  max(self.tree[2*index],self.tree[2*index+1])
            if updatedValue == self.tree[index]:
                break # We can do this without the if contiotion too, but this is faster
            self.tree[index] = updatedValue

    # Example query, leftmost larger than x value
    def query(self, value):
        if self.tree[1] < value: # Because this is max tree and query value is larger than max root node
            return -1                                # then it means such value doesnt exist in the data

        index = 1 # Because we will walk down from root
        left, right = 0, self.size - 1

        while index < self.size:
            mid = (left + right) // 2
            if self.tree[mid] >= value:
                index = 2*index
                right = mid//2
            else:
                index = 2*index + 1
                left = mid//2 + 1

        relativeIndex = index - self.size
        return relativeIndex if relativeIndex < self.n else -1
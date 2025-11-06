class Node:
    def __init__(self, key, val):
        self.key: int = key
        self.val: int = val
        self.next: Node = None
        self.prev: Node = None

class LRUCache:

    def __init__(self, capacity: int):
        self.n = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def insertNode(self, node: Node): # Most Recent
        left = self.right.prev
        left.next = node
        node.prev = left
        node.next = self.right
        self.right.prev = node

    def removeNode(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        valToReturn = node.val
        self.removeNode(node)
        self.insertNode(node)
        return valToReturn

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insertNode(self.cache[key])

        if len(self.cache) > self.n:
            leftMost = self.left.next
            del self.cache[leftMost.key]
            self.removeNode(leftMost)
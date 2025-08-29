# Initial approach
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minVal = min(self.getMin(),val) if self.stack else val
        self.stack.append([val,minVal])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# Just modified init and push so there is no extra if check
class MinStack:

    def __init__(self):
        self.stack = [[None,float("inf")]]

    def push(self, val: int) -> None:
        minVal = min(self.getMin(),val)
        self.stack.append([val,minVal])



# Uinsg the diff stack method
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        return self.stack[-1] + self.min if self.stack[-1] > 0 else self.min

    def getMin(self) -> int:
        return self.min
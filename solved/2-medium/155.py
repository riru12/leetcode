class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        if self.stack.pop() == self.min:
            self.min = float('inf')
            for i in range(len(self.stack)):
                if self.stack[i]<self.min:
                    self.min = self.stack[i]

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
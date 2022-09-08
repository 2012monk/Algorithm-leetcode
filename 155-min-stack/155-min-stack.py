class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.m = float('inf')

    def push(self, val: int) -> None:
        if val <= self.m:
            self.s.append(self.m)
            self.m = val
        self.s.append(val)
        

    def pop(self) -> None:
        if self.m == self.s.pop():
            self.m = self.s.pop()
        

    def top(self) -> int:
        if self.s:
            return self.s[-1]
        

    def getMin(self) -> int:
        return self.m
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
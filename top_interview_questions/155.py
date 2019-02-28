class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x: 'int') -> 'None':
        if len(self.s1) == 0:
            self.s1.append(x)
            self.s2.append(x)
        else:
            self.s1.append(x)
            self.s2.append(min(x, self.s2[-1]))
        
    def pop(self) -> 'None':
        if len(self.s1) == 0:
            return None
        else:
            self.s2.pop()
            return self.s1.pop()
        
        

    def top(self) -> 'int':
        if len(self.s1) == 0:
            return None
        return self.s1[-1]
        

    def getMin(self) -> 'int':
        if len(self.s2) == 0:
            return None
        else:
            return self.s2[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
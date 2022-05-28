class MaxStack:

    def __init__(self):
        self.stack = []
        self.max = [float('-inf')]
        
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.max.append(max(self.max[-1], x))
        

    def pop(self) -> int:
        self.max.pop()
        return self.stack.pop()
        
        
    def top(self) -> int:
        return self.stack[-1]
        

    def peekMax(self) -> int:
        return self.max[-1]
        

    def popMax(self) -> int:
        max_val = self.max[-1]
        temp = []
        for i in range(len(self.stack)-1, -1, -1):
            cur = self.pop()
            if cur == max_val:
                break
            else:
                temp.append(cur)
  
        for n in reversed(temp):
            self.push(n)

        return max_val
        

        
        
        
#     def __init__(self):
#         self.stack = []
        
        
#     def push(self, x: int) -> None:
#         self.stack.append(x)
        

#     def pop(self) -> int:
#         return self.stack.pop()
        
        
#     def top(self) -> int:
#         return self.stack[-1]
        

#     def peekMax(self) -> int:
#         return max(self.stack)
        

#     def popMax(self) -> int:
#         max_val = max(self.stack)
        
#         for i in range(len(self.stack)-1, -1, -1):
#             if self.stack[i] == max_val:
#                 del self.stack[i]
#                 return max_val

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
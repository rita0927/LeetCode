class MyStack:

    def __init__(self):
        self.q1 = deque()


    def push(self, x: int) -> None:
        self.q1.append(x)
        self.q1.rotate(1)

    def pop(self) -> int:
        return self.q1.popleft()
        

     
    def top(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        return not self.q1 
        
        














# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



# class MyStack:

#     def __init__(self):
#         self.queue = deque()
        

#     def push(self, x: int) -> None:
#         self.queue.append(x)
        
#         # rotate with positive int (default is 1): move from right to left
#         self.queue.rotate(1)
        
#         # n = len(self.queue) 
#         # while n > 1:
#         #     self.queue.append(self.queue.popleft())
#         #     n -= 1

#     def pop(self) -> int:
#         return self.queue.popleft()
        

#     def top(self) -> int:
#         return self.queue[0]
        

#     def empty(self) -> bool:
#         return not self.queue







# class MyStack:

#     def __init__(self):
#         self.q1 = deque()
#         self.q2 = deque()
#         self.last = None 
        

#     def push(self, x: int) -> None:
#         self.q1.append(x)
#         self.last = x
        

#     def pop(self) -> int:

#         while len(self.q1)> 1:
#             self.last = self.q1.popleft()
#             self.q2.append(self.last)
            
#         res = self.q1.popleft()
#         self.q1, self.q2 = self.q2, self.q1
#         return res 

#     def top(self) -> int:
        
#         return self.last
        

#     def empty(self) -> bool:
#         return not self.q1
        
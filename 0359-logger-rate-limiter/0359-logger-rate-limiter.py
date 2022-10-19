class Logger:
    
    
    def __init__(self):
        self.set=set()
        self.queue=deque()

        
    def shouldPrintMessage(self, timestamp, message):
        while self.queue and timestamp-self.queue[0][1]>=10:
            msg, time=self.queue.popleft()
            self.set.remove(msg)
        
        if message in self.set:
            return False
        else:
            self.set.add(message)
            self.queue.append((message, timestamp))
            return True


















# class Logger:
    
    
#     def __init__(self):
#         self.set = set()
#         self.queue = deque()
        
#     def shouldPrintMessage(self, timestamp, message):
#         while self.queue and timestamp - self.queue[0][1] >= 10:
#             msg, time = self.queue.popleft()
#             self.set.remove(msg)
        
#         if message in self.set:
#             return False
#         else:
#             self.set.add(message)
#             self.queue.append((message, timestamp))
#             return True 
            

























# class Logger:

#     def __init__(self):
#         self.d = dict()
           

#     def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
#         if message not in self.d or (message in self.d and timestamp - self.d[message] >=10):
#             self.d[message]=timestamp
#             return True 
#         else:
#             return False

         

        
        
        
        
        
        
        
        
        
        
        

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
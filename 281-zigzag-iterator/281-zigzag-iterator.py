class ZigzagIterator:
    
    def __init__(self, v1: List[int], v2: List[int]):
        self.lst = [v1, v2]
        self.queue = deque()
        
        for i, v in enumerate(self.lst):
            if v:
                self.queue.append([i, 0])

        
    def next(self) -> int:
        i, v_idx = self.queue.popleft()
        
        if v_idx + 1 < len(self.lst[i]):
            self.queue.append([i, v_idx+1])
        return self.lst[i][v_idx]
        

    def hasNext(self) -> bool:
        return self.queue
        
        
      
    
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())




# class ZigzagIterator:
    
#     # space O(k) where k is the number of input vectors (assume more than two vectors)
#     def __init__(self, v1: List[int], v2: List[int]):
        
#         self.lst = [v1,v2]
#         self.queue = deque()

#         for index, v in enumerate(self.lst):
#             # only insert vectors with element, not empty vector
#             if v:
#                 # append the vector index in the self.lst and the element index in the vector
#                 self.queue.append((index, 0))

#     # time: O(1) 
#     def next(self) -> int:
#         if self.queue:
#             v_idx, el_idx = self.queue.popleft()
#             next_el_idx = el_idx + 1
#             # append the vector index and next element index back to queue if the next element exists 
#             if  next_el_idx < len(self.lst[v_idx]):
#                 self.queue.append((v_idx, next_el_idx))
#             return self.lst[v_idx][el_idx]

#     def hasNext(self) -> bool:
#         return self.queue
       
















# class ZigzagIterator:
#     def __init__(self, v1: List[int], v2: List[int]):
#         self.v1 = v1
#         self.v2 = v2
#         self.i1 = 0 
#         self.i2 = 0
#         self.next_is_v1 = True
    
    
#     # O(1), O(1) for two input vectors 
#     def next(self) -> int:
#         if self.next_is_v1 and self.i1 < len(self.v1):
#             res = self.v1[self.i1]
#             self.i1 += 1
#             if self.i2 < len(self.v2):
#                 self.next_is_v1 = False
#             return res 
#         else:
#             res = self.v2[self.i2]
#             self.i2 += 1
#             if self.i1 < len(self.v1):
#                 self.next_is_v1 = True 
#             return res    

#     def hasNext(self) -> bool:
#         return self.i1 < len(self.v1) or self.i2 < len(self.v2)
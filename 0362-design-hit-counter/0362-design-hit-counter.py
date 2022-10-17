# class HitCounter:
    
#     def __init__(self):
 

#     def hit(self, timestamp: int) -> None:


#     def getHits(self, timestamp: int) -> int:
        

        
class HitCounter:
    def __init__(self):
        self.hits=[]
        
    def hit(self, timestamp):
        if self.hits and self.hits[-1][0]==timestamp:
            self.hits[-1][1]+=1
        else:
            self.hits.append([timestamp, 1])
    
    def getHits(self, timestamp):
        l=-1
        r=len(self.hits)
        
        while l+1!=r:
            mid=(l+r)//2
            if timestamp-300>=self.hits[mid][0]:
                l=mid
            else:
                r=mid
        self.hits=self.hits[r:]
        return sum(x[1] for x in self.hits)
        
        
        
        
        
        
        
        
        
        
        
        



# class HitCounter:
    
#     def __init__(self):
#         self.hits = []


#     def hit(self, timestamp: int) -> None:
#         if self.hits and self.hits[-1][0] == timestamp:
#             self.hits[-1][1] += 1
#         else:
#             self.hits.append([timestamp, 1])

#     def getHits(self, timestamp: int) -> int:
        
#         l = -1
#         r = len(self.hits)
        
#         while l+1 != r:
#             mid = (l+r)//2
            
#             if self.hits[mid][0] <= timestamp - 300:
#                 l = mid 
#             else:
#                 r = mid
#         # remove the expired (300 sec ago) timestamps 
#         self.hits = self.hits[r:]
#         return sum(x[1] for x in self.hits)
        



# class HitCounter:

#     # space: O(N) in the case of repetitions in the same timestamp, the space required for storing those values O(1)
    
#     def __init__(self):
#         self.queue = deque()
#         # self.count = 0

#     def hit(self, timestamp: int) -> None:
#         if self.queue and timestamp == self.queue[-1][0]:
#             self.queue[-1][1] += 1
#         else:
#             self.queue.append([timestamp, 1])
#         # self.count+=1
        
#     # time: O(logN) with binary search, otherwise O(N) 
#     def getHits(self, timestamp: int) -> int:
        
#         l = -1 
#         r = len(self.queue)
        
#         # find the cut off of the past 300 sec, [r, timestamp]
#         while l + 1 != r:
#             mid = (l+r)//2
            
#             if self.queue[mid][0] <= timestamp - 300:
#                 l = mid
#             else:
#                 r = mid
                
#         return sum([self.queue[i][1] for i in range(len(self.queue)) if i >= r])

        
# #         while self.queue and self.queue[0][0] <= timestamp - 300:
# #             t,c = self.queue.popleft()
# #             self.count -= c
# #         return self.count 
            
    

            

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
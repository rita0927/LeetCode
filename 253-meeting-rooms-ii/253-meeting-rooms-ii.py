class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [(intervals[0][1])]
        res = 1
        for start, end in intervals[1:]:
            if start < heap[0]:
                res += 1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        
        return len(heap)
                
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(NlogN) due to sort and heap operation, O(N)        
#         rooms = 0
#         starts = sorted([interval[0] for interval in intervals])
#         ends = sorted([interval[1] for interval in intervals])
        
#         e = 0
        
#         for s in range(len(intervals)):
#             if starts[s] >= ends[e]:
#                 rooms -=1
#                 e +=1
#             rooms +=1
        
#         return rooms
                
        
        
  
        
        
        
        
        
        
        
        
        
        
      
        
        
        
#         # O(NlogN) due to sort and heap operation, O(N)
        
#         # use heap to store the sorted end time
#         intervals.sort()
#         rooms = []
        
#         heapq.heappush(rooms, intervals[0][1])
        
#         for start, end in intervals[1:]:
            
#             if start >= rooms[0]:
#                 heapq.heappop(rooms)
            
#             heapq.heappush(rooms, end)
#         return len(rooms)
        
        
            
            
            
            
        
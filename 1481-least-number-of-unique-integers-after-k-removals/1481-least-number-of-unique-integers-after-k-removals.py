class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = list(Counter(arr).values())
        heapq.heapify(count)

        while k:
            k -= heapq.heappop(count)
            
            if k <0:
                return len(count) + 1
            
        return len(count)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         count = list(Counter(arr).values())

#         heapq.heapify(count)

#         while k:
#             k -= heapq.heappop(count)

#             if k < 0:
#                 return len(count) + 1

#         return len(count)
            
        
            
        
        
        
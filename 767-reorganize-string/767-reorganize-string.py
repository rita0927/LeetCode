class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-count[c], c) for c in count]
        heapq.heapify(heap)
        
        prev = None
        res = ''
        
        while heap or prev:
            if prev and not heap:
                return ''
   
            count_cur, cur = heapq.heappop(heap)
            res += cur
            count_cur += 1
            
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            if count_cur:
                prev = (count_cur, cur)
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     # O(nlogn), O(n)
#     def reorganizeString(self, s: str) -> str:
#         count = Counter(s)
#         heap = []
#         for c in count:
#             if count[c] >(len(s) + 1)//2:
#                 return ''
            
#             # max heap to store the count from more frequent to less frequent
#             heapq.heappush(heap, (-count[c], c))
        
#         prev = None
#         res = ''
        
#         while heap or prev:

#             cur_count, cur = heapq.heappop(heap)
#             res += cur
#             # cu_count is negative, += 1 means decrease the absolute count
#             cur_count += 1
            
#             if prev:
#                 heapq.heappush(heap, prev)
#                 prev = None
#             if cur_count:
#                 prev = (cur_count, cur)
#         return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         heap = []
#         count = Counter(s)
#         for c in count.keys():
#             if count[c] > (len(s) + 1)//2:
#                 return ''
#             heapq.heappush(heap, (-count[c],c))
        
#         prev_count, prev = heapq.heappop(heap)
#         res = [prev]
#         while heap:
#             next_count, next = heapq.heappop(heap)
#             res.append(next)
#             if -prev_count > 1:
#                 heapq.heappush(heap, (prev_count + 1, prev))
#             prev_count, prev = next_count, next
#         return "".join(res)
        
        
        
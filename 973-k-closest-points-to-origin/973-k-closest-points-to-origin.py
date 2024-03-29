class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        
        for p in points:
            x,y = p
            distance = x ** 2 + y ** 2
            if len(heap) == k:
                heapq.heappushpop(heap, (-distance, p))
            else:
                heapq.heappush(heap, (-distance, p))
                
        return [p[1] for p in heap]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         # O(Nlog(k))   
#         return heapq.nsmallest(k, points, key = lambda x: x[0] ** 2 + x[1] ** 2)
        

        
        
     
        
        
#         heap = []
        
#         for (x,y) in points:
#             squaredDistance = -(x**2 + y**2)
            
#             if len(heap) == k:
#                 heapq.heappushpop(heap, (squaredDistance, x, y))
#             else:
#                 heapq.heappush(heap, (squaredDistance, x, y))
            
#         return [(x,y) for (squaredDistance, x, y) in heap]
        
  


        
        
        
#         distances = sorted(points, key = lambda x: x[0] **2 + x[1] **2)
        
#         return distances[:k]
        
    
    
    
    
        
#         points.sort(key = lambda x: x[0]**2 + x[1]**2)

#         return points[:k]


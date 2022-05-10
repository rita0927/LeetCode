class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        prevEnd = points[0][1]
        res = 1
        
        for start, end in points[1:]:
            if start > prevEnd:
                res +=1
                prevEnd = end
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(nlogn), O(n) becuase of sorting
        
#         #Method 1: sort by start
        
#         points.sort()
#         res = 1 
#         prevEnd = points[0][1]
        
#         for start, end in points[1:]:
#             if start > prevEnd:
#                 res +=1
#                 prevEnd = end
#             else:
#                 prevEnd = min(prevEnd, end)
#         return res 
                
        
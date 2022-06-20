class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start >= prev:
                prev = end
            else:
                prev = min(prev, end)
                res += 1
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(nlogn), O(1)
#         intervals.sort()
#         prevEnd = intervals[0][1]
#         res = 0
#         for start, end in intervals[1:]:
#             if start >=prevEnd:
#                 prevEnd = end
#             else:
#                 res +=1
#                 prevEnd = min(prevEnd, end)
#         return res 
        
        
        
        
        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        res = []
        
        for s, e in intervals:
            if res and res[-1][1] >= s:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s,e])
        return res 
                
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         intervals.sort()
        
#         stack = []
        
#         for start, end in intervals:
            
#             if stack and stack[-1][1] >= start:
#                 stack[-1][1] = max(end, stack[-1][1])
#             else:
#                 stack.append([start, end])
#         return stack 
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # O(nlogn), O(logn) for sorting itself
#         intervals.sort()
#         stack = []
        
        
#         for start, end in intervals:
            
#             if stack and stack[-1][1] >= start:
#                 interval = stack.pop()
#                 end = max(end, interval[1])
#                 stack.append([interval[0], end])
#             else:
#                 stack.append([start, end])
            
#         return stack 
                        
            
        
        
        
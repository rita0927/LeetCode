class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        stack = [[intervals[0][0], intervals[0][1]]]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            if start <= stack[-1][1]:
                stack[-1][1] = max(end, stack[-1][1])
            
            else:
                stack.append(intervals[i])
        return stack
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
                        
            
        
        
        
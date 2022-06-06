class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        stack = []
        
        for interval in intervals:
            start, end = interval
            
            if stack and stack[-1][1] >= start:
                stack[-1][1] = max(end, stack[-1][1])        
            else:
                stack.append(interval)
                
        return stack
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
                        
            
        
        
        
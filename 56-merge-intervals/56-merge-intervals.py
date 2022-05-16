class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        stack = []
        
        
        for start, end in intervals:
            
            if stack and stack[-1][1] >= start:
                interval = stack.pop()
                start = min(interval[0], start)
                end = max(interval[1], end)
                
            stack.append([start, end])
            
        return stack 
                        
            
        
        
        
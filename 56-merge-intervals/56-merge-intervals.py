class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        stack = []
        
        
        for start, end in intervals:
            
            if stack and stack[-1][1] >= start:
                interval = stack.pop()
                end = max(end, interval[1])
                stack.append([interval[0], end])
            else:
                stack.append([start, end])
            
        return stack 
                        
            
        
        
        
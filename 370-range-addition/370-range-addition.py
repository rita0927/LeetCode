class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        res = [0] * length
        
        for start, end, inc in updates:
            res[start] += inc
            
            if end + 1< length:
                res[end + 1] -= inc
        
        for i in range(1,length):
            res[i]+= res[i-1]
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = [0] * length
        
#         for start, end, inc in updates:
#             for i in range(start, end+1):
#                 res[i] +=inc
#         return res 
        
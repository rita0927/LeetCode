class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        res = ''
        inc = 2 * (numRows - 1)
        for r in range(numRows):
            for i in range(r, len(s), inc):
                res += s[i]
                
                if r > 0 and r < numRows-1 and i+inc-2*r < len(s):
                    res += s[i+inc-2*r]
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if numRows == 1: return s
        
#         res = ""
#         for r in range(numRows):
#             increment = 2 * (numRows - 1)
#             for i in range(r, len(s), increment):
#                 res +=s[i]
                
#                 # middle rows hve one more ch between the increment
#                 # exclude the first and the last row
#                 if (r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s)):
#                     res +=s[i + increment - 2 * r ]
#         return res 
                    
            
        
        
        
        
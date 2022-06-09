class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
        for ch in s:
            
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])
            else:
                stack[-1][1] += 1
                
                if stack[-1][1] == k:
                    stack.pop()
        
        res = ''
        
        for ch, count in stack:
            res += ch * count 
        
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(N), O(N)
#         stack = []

#         for ch in s:
            
#             if not stack or stack[-1][0] != ch:
#                 stack.append([ch, 1])

#             else:
#                 stack[-1][1] += 1
#                 if stack[-1][1] == k:
#                     stack.pop()
#         res = ''
#         for ch, count in stack:
#             res += ch * count 
        
#         return res 
            
                
                
        
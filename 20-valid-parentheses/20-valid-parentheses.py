class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')':'(',
            ']':'[',
            '}': '{'     
        }
        
        stack = []
        
        for p in s:
            if p in d:
                if stack and stack.pop() == d[p]:
                    continue
                else:
                    return False 
            else:
                stack.append(p)
        return not stack 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = {')':'(',
#              '}': '{',
#              ']': '['}
        
#         stack = []
        
#         for p in s:
#             if p in d:
#                 if stack and stack[-1] == d[p]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(p)
                
#         return not stack
  
                
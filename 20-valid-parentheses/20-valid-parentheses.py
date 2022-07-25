class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        stack = []
        
        for p in s:
            if not p in d:
                stack.append(p)
            else:
                if not stack or stack[-1] != d[p]:
                    return False 
                else:
                    stack.pop()
        return not stack 
            

        


                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = {
#             ')':'(',
#             ']':'[',
#             '}': '{'     
#         }
        
#         stack = []
        
#         for p in s:
#             if p in d:
#                 if stack and stack.pop() == d[p]:
#                     continue
#                 else:
#                     return False 
#             else:
#                 stack.append(p)
#         return not stack 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
  
                
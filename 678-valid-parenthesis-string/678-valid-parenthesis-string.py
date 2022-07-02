class Solution:
    def checkValidString(self, s: str) -> bool:
        
        count = []
        stack = []
        
        for i,p in enumerate(s):
            if p == '(':
                stack.append(i)
            elif p == ')':
                if not stack and not count:
                    return False
                elif not stack:
                    count.pop()
                else:
                    stack.pop()
            else:
                count.append(i)
                
        while count and stack:
            if stack.pop() > count.pop():
                return False
        
        return not stack
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#     # O(n), O(1)        
#         # keep track of max & min count of balanced open parenthesis 
#         # maintain a range of balanced open parenthesis 
#         low = 0
#         high = 0
        
#         for p in s:
#             if p == '(':
#                 low += 1
#                 high += 1
                
#             # deduct the count of balanced open parenthesis
#             elif p == ')':
#                 low -= 1
#                 high -= 1
                
#             # when p == * 
#             else:
                
#                 # treat * as )
#                 low -= 1
#                 # treat * as (
#                 high += 1
            
#             # low can't be less than 0
#             # if it's negative, reset to 0
            
#             low = max(low, 0)
            
#             # if high is zero, there're unbalanced ), which can't be balanced later 
#             # example ))**
            
#             if high < 0:
#                 return False
            
#         # low is always >= 0
#         # If low > 0, balanced parenthesis is not in the range, and there're always extra (
#         return low == 0       


    
    
    
    
    
    
    
    
    
    
    
    
    
    
  






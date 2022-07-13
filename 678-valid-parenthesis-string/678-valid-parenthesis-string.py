class Solution:
    def checkValidString(self, s: str) -> bool:
        
        star = []
        left = []
        
        for i, p in enumerate(s):
            if p == '*':
                star.append(i)
            elif p == '(':
                left.append(i)
            else:
                if not star and not left:
                    return False
                elif left:
                    left.pop()
                else:
                    star.pop()
        
        while left and star:
            if star.pop() < left.pop():
                return False
            
        return not left 
        
        

                    
                
                
                
                
                
                
                
                
                
                
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n), O(n)
        
#         # record the index of '*'
#         count = []
#         # record the index of '('
#         stack = []
        
#         for i,p in enumerate(s):
#             if p == '(':
#                 stack.append(i)
                
#             elif p == ')':
                
#                 # when there's no '*' or  '(' before the '),' impossible to form a balanced parenthesis
#                 if not stack and not count:
#                     return False
                
#                 # only '*' available, use '*' to offset ')' 
#                 elif not stack:
#                     count.pop()
                    
#                 # if stack is avaialble (regardless of count), pop stack to offset ')'
#                 else:
#                     stack.pop()
                    
#             # if p == '*'
#             else:
#                 count.append(i)
                
#         # if there're extra stack & count, '*' must be after '(' in order to offset/balance     
#         while count and stack:
            
#             # if '(' is after '*', 
#             # example **((, count = [0,1], stack = [2,3]
#             if stack.pop() > count.pop():
#                 return False
            
#         # stack must be empty, no extra '('
#         # otherwise, there isn't emough ')' or '*' to balance the '('
#         return not stack
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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


    
    
    
    
    
    
    
    
    
    
    
    
    
    
  






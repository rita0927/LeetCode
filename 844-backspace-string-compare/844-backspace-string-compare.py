class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(string):
            stack = []
            for i in string:
                if stack and i == '#':
                    stack.pop()
                elif i != '#':
                    stack.append(i)
                    
            return ''.join(stack)
        
        return helper(s) == helper(t)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def helper(string):
#             stack = []
            
#             for i in string:
#                 if i != '#':
#                     stack.append(i)
#                 # i == '#' and stack is not empty
#                 elif stack:
#                     stack.pop()

#             return ''.join(stack)
                    
#         return helper(s) == helper(t)
        
        
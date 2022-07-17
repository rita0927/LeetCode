class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        l = 0
        r = 0
        
        def backtrack(path):
            nonlocal l,r
            
            if len(path) == 2 * n:
                res.append(''.join(path))
                return 
            
            if l < n:
                path.append('(')
                l+=1
                backtrack(path)
                path.pop()
                l -= 1
            
            if r < l:
                path.append(')')
                r += 1
                backtrack(path)
                path.pop()
                r -= 1
        backtrack([])
        return res 
            
            
        
        



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#        # O(4^n / n^0.5), O(4^n / n^0.5)
        
#         res = []
        
#         def backtrack(path,l,r):
            
#             if l+r == 2 *n:
#                 res.append(''.join(path))
#                 return
            
#             if l < n:
#                 path.append('(')
#                 backtrack(path,l+1,r)
#                 path.pop()
                
#             if r < l:
#                 path.append(')')
#                 backtrack(path, l, r+1)
#                 path.pop()
        
#         backtrack([],0,0)
#         return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack = []
#         result = []

#         def backtrack(openCount, closeCount):

#             if openCount == closeCount == n:

#                 result.append("".join(stack))
#                 return

#             if openCount < n:
#                 stack.append("(")
#                 backtrack(openCount + 1, closeCount)
#                 stack.pop()

#             if closeCount < openCount:
#                 stack.append(")")
#                 backtrack(openCount, closeCount + 1)
#                 stack.pop()

#         backtrack(0, 0)
#         return result
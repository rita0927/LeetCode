class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        s = list(s)
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        for j in stack:
            s[j] = ''
        
        return ''.join(s)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n), O(n)
#         stack = []
#         s = list(s)
        
#         for i in range(len(s)):
#             if s[i] == '(':
#                 stack.append(i)
#             elif s[i] == ')':
#                 if stack:
#                     stack.pop()
#                 else:
#                     s[i] = ''
#         for j in stack:
#             s[j] = ''
        
#         return ''.join(s)
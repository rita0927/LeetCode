class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        res = 0
        stack = [-1]
        
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i-stack[-1])
        return res 
        
        
        
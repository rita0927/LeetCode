class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != ")":
                stack.append(s[i])
            
            else:
                temp = ""
                while stack and stack[-1] != "(":
                    temp +=stack.pop()
                
                stack.pop()
                
                for ch in temp:
                    stack.append(ch)
                
        return "".join(stack)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 
        
        
        
#         opens = []
#         i = 0
        
#         while i < len(s):
#             if s[i] == "(":
#                 opens.append(i)
#                 i+=1
#             elif s[i] == ")":
#                 start = opens.pop()
#                 sub = s[start + 1:i]
#                 sub = sub[::-1]
#                 s = s[:start] + sub + s[i + 1:]
#                 i-=1
#             else:
#                 i +=1
                
#         return s
        
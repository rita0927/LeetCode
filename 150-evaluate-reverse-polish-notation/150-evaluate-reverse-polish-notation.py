class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for i in tokens:    
            if i in '+-*/':
                n1 = stack.pop()
                n2 = stack.pop()
                
                if i == '+':
                    stack.append(n1 + n2)
                elif i == '-':
                    stack.append(n2-n1)
                elif i == '*':
                    stack.append(n1 * n2)
                elif i =='/':
                    stack.append(int(n2/n1))
            else:
                stack.append(int(i))
            
        return stack[0]
        
        

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack = []

#         for t in tokens:
#             if t in "+-*/":
#                 a = stack.pop()
#                 b = stack.pop()
#                 if t == "+":
#                     stack.append(a + b)
#                 elif t == "-":
#                     stack.append(b - a)
#                 elif t == "*":
#                     stack.append(a * b)
#                 else:
#                     stack.append(trunc(b / a))
#             else:
#                 stack.append(int(t))
#         return stack[0]
        
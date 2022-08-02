class Solution:
    def calculate(self, s: str) -> int:
        
        if not s:
            return 0
        
        cur = 0
        prev = 0
        res = 0
        operators = '+-*/'
        operator = '+'
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                cur = cur * 10 + int(ch)
                
            if ch in operators or i == len(s)-1:
                if operator in '+-':
                    res += prev 
                    prev = cur if operator == '+' else -cur
                elif operator == '*':
                    prev *= cur
                elif operator == '/':
                    if prev > 0:
                        prev //= cur
                    else:
                        prev= -(-prev//cur)
                operator = ch 
                cur = 0
        
        res += prev 
        return res 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack = []
#         num = 0
#         operators = {'+', '-', '*', '/'}
#         # keep track of previous operator
#         operator = '+'
        
#         for i in range(len(s)):
#             l = s[i]
            
#             if l.isdigit():
#                 num = num * 10 + int(l)
            
#             if l in operators or i == len(s) - 1:
#                 if operator == '+':
#                     stack.append(num)
#                 if operator == '-':
#                     stack.append(-num)
#                 if operator == '*':
#                     num *= stack.pop()
#                     stack.append(num)
#                 if operator == '/':
#                     pre = stack.pop()
#                     if pre > 0:
#                         stack.append(pre//num)
#                     else:
#                         stack.append(-(-pre//num))      
                
#                 operator = l
#                 num = 0
#         return sum(stack)
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#       stack = []
#       operators = {'+', '-', '*', '/'}
#       sign = '+'
#       tmp = 0
#       for i in range(len(s)):
#         letter = s[i]
#         if letter.isdigit():
#           tmp = tmp*10 + int(letter)
#         if letter in operators or i == len(s) -1:
#           if sign == '+':
#             stack.append(tmp)
#           if sign == '-':
#             stack.append(-tmp)
#           if sign=='*':
#             tmp=tmp*stack.pop()
#             stack.append(tmp)
#           if sign == '/':
#             vertex = stack.pop()
#             if vertex > 0:
#               stack.append(vertex//tmp)
#             else:
#               stack.append(-1*((-vertex)//tmp))
#           sign = letter
#           tmp = 0
#       return sum(stack)
        
class Solution:
    def decodeString(self, s: str) -> str:
        string = ''
        count = 0
        stack = []
        
        
        for i in s:
            if i.isdigit():
                count = count * 10 + int(i)
            elif i =='[':
                stack.append(string)
                string = ''
                stack.append(count)
                count = 0 
            elif i == ']':
                num = stack.pop()
                prev = stack.pop()
                string = prev + num * string
            else:
                string += i
            
        return string 
                
                
                
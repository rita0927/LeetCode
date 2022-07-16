class Solution:
    def myAtoi(self, s: str) -> int:
        
        if not s:
            return 0
        
        i = 0
        
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0
        
        isPos = True 
        if s[i] == '-' or s[i] == '+':
            isPos = False if s[i] == '-' else True 
            i += 1

        res = 0
        while i < len(s):
            if not s[i].isdigit():
                break
            res = res * 10 + int(s[i])
            if isPos and res > 2**31 - 1:
                return 2**31 - 1
            
            if not isPos and res > 2**31:
                return -2**31
            i+=1
            
        return res if isPos else -res 
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stripS = s.strip()
#         if stripS == "" or stripS == "-" or stripS == "+":
#             return 0

#         s1 = re.match("[^\d+]+", (stripS.lstrip("-")).lstrip("+"))

#         if s1 != None:
#             return 0

#         else:
#             s1 = re.search("\-*\+*\d+", stripS).group()

#         if s1[0:2] == "--" or s1[0:2] == "-+" or s1[0:2] == "++":
#             return 0
#         result = int(s1)
#         if result > 0:
#             return 2147483647 if result > 2147483647 else result
#         else:
#             return -2147483648 if result < -2147483648 else result
        
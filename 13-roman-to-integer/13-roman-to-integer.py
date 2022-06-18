class Solution:
    def romanToInt(self, s: str) -> int:
        
        
        
        # O(1) due to limited Roman Numbers, O(1)
        d = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1         
        }
        
        res = 0
        i = 0
        while i < len(s):
            if i+1 <len(s) and s[i:i+2] in d:
                res += d[s[i:i+2]]
                i+=2
            else:
                res += d[s[i]]
                i+=1 
        return res 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         obj = {'I': 1,
#                'V': 5,
#                'X': 10,
#                'L': 50,
#                'C': 100,
#                'D': 500,
#                'M': 1000 }
        
        
#         res = 0
        
#         for i in range(len(s) -1):
#             if obj[s[i]] < obj[s[i+1]]:
#                 res = res - obj[s[i]]
#             else: 
#                 res += obj[s[i]]
            
#         res += obj[s[-1]]
#         return res 
    

    
            
            
        
        
        
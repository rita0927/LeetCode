class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         s.strip()
#         res = []
#         temp = ''
        
#         for i in s:
#             if i == ' ':
#                 if temp:
#                     res.append(temp)
#                     temp = ''
#             else:
#                 temp += i
        
#         if temp:
#             res.append(temp)
        
#         return ' '.join(reversed(res))
                
        
        
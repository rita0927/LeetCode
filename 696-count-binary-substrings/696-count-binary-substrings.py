class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        res, prev, cur = 0,0,1
        
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                res += min(prev, cur)
                prev = cur
                cur = 1
            
            else:
                cur +=1
        return res + min(prev, cur)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(N), O(1)
#         res, prev, cur = 0,0,1
        
#         for i in range(1, len(s)):
#             if s[i] != s[i-1]:
#                 res += min(prev, cur)
#                 prev = cur
#                 cur = 1
  
#             else:
#                 cur +=1
            
#         return res + min(prev, cur)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(N), O(N)
#         count = [1]
#         res = 0
#         for i in range(1, len(s)):
#             if s[i] != s[i-1]:
#                 count.append(1)
#             else:
#                 count[-1]+=1

#         for i in range(1, len(count)):
#             res += min(count[i], count[i-1])
            
#         return res 
            
        
        
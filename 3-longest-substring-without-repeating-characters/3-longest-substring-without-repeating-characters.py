class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        l = 0
        res = 0
        dic = defaultdict(int)
        
        for r in range(len(s)):
            
            if s[r] in dic:
                l = max(dic[s[r]] + 1, l) 
                
            dic[s[r]] = r
            res = max(res, r-l+1)
            
        return res 
        

            
            
 

































           

#         sub = set()
#         res = 0
#         l = 0
        
#         for r in range (len(s)):
#             while s[r] in sub:
#                 sub.remove(s[l])
#                 l+=1
#             sub.add(s[r])
#             res = max(res, r-l+1)
#         return res
                
                
# #O(n), O(n)
        
#         def check(start, end):
#             sub = set()
#             for i in range(start, end+1):
#                 if s[i] in sub:
#                     return False
#                 sub.add(s[i])
#             return True
#         res = 0
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if check(i, j):
#                     res = max(res, j-i+1)
#         return res 

# # O(n^3) ETL
            
            
        
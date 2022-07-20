from functools import *

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        A= len(s1)
        B = len(s2)
        C = len(s3)
        
        if A+B != C:
            return False 
        
        i1 = 0
        i2 = 0
        i3 = 0
        
        @lru_cache
        def helper(i1,i2,i3):
            if i3 == C:
                return True
            
            p1 = False
            p2 = False
            if i1 < A and s1[i1] == s3[i3]:
                p1 = helper(i1+1, i2, i3+1)
            
            if i2 < B and s2[i2] == s3[i3]:
                p2 = helper(i1, i2+1, i3+1)
            
            return p1 or p2 
        
        return helper(0,0,0)
                
            
            
        

        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(s1) + len(s2) != len(s3):
#             return False 
        
#         @lru_cache
#         def helper(i1,i2,i3):
#             if i3 == len((s3)):
#                 return True
            
#             path1 = False
#             path2 = False
#             if i1 < len(s1) and s1[i1] == s3[i3]:
#                 path1 = helper(i1 + 1, i2, i3+1)

#             if i2 < len(s2) and s2[i2] == s3[i3]:
#                 path2 = helper(i1, i2+1, i3+1)
            
#             return path1 or path2
        
#         return helper(0,0,0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#   # O(m*n)), O(m*n)
#         A = len(s1)
#         B = len(s2)
#         C = len(s3)
#         if A+B != C: return False 
        
#         @lru_cache 
#         def helper(i1, i2, i3):
            
#             if i3 == C:
#                 return True
#             p1 = False
#             p2 = False
#             if i1 < A and s1[i1] == s3[i3]:
#                 p1 = helper(i1+1, i2, i3+1)
#             if i2 < B and s2[i2] == s3[i3]:
#                 p2 = helper(i1, i2+1, i3+1)
#             return p1 or p2 
#         return helper(0,0,0)
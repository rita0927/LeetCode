class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
#         n = len(s)
#         """
#         Search a substring of given length
#         that occurs at least 2 times.
#         @return start position if the substring exits and -1 otherwise.
#         """
        
#         def helper(length):
#             seen = set()
#             for i in range(n-length+1):
#                 sub = s[i:i+length]
#                 if sub in seen:
#                     return i
#                 seen.add(sub)
#             return -1
        

#         l,r = 1, n
#         while l <=r:
#             mid = l + (r-l)//2
#             if helper(mid) != -1:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return l - 1
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if len(s) < 2:
            return 0
        
        seen = set()
        res = 0
        
        # for r in range(1,len(s)+1):
        #     for l in range(r):
        for l in range(len(s)):
            for r in range(l+1, len(s)+1):
                if s[l:r] in seen:
                    res = max(res, r-l)
                else:
                    seen.add(s[l:r])
             
        
        return res 
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s) 
        """
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        # find repeating substring 
        def helper(length):
            seen = set()
            for i in range(n-length):
                sub = s[i:i+length+1]
                if sub in seen:
                    return True
                seen.add(sub)
            return False 
        

        l,r = 0, n -1
        while l <=r:
            # avoid overflow
            mid = l + (r-l)//2
            if helper(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l 
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#   # O(n^3), O(n^3) since the slice is O(n) space complexity       
#         if len(s) < 2:
#             return 0
        
#         seen = set()
#         res = 0
        
#         # for r in range(1,len(s)+1):
#         #     for l in range(r):
#         for l in range(len(s)):
#             # r is exclusive
#             for r in range(l+1, len(s)+1):
#                 if s[l:r] in seen:
#                     res = max(res, r-l)
#                 else:
#                     seen.add(s[l:r])
        
#         return res 
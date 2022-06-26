class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:

        
        """
        a b c x y z 1 2 3
        T T T T F F T T T 
       <b>   </b>  <b> </b>        
        """
        n = len(s)
        buckets = [False] * n
        l = 0
        
        for l in range(n):
            r = 0
            for w in words:
                if s.startswith(w,l):
                    r = max(r, l+len(w))
            for i in range(l,r):
                buckets[i] = True 
            
        
        res = ''
        
        for i in range(n):
            if buckets[i] and (i == 0 or i >0 and not buckets[i-1]):
                res += '<b>'
            res += s[i]
            if buckets[i] and (i == n-1 or i < n - 1 and not buckets[i+1]):
                res += '</b>'
        return res 
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(s)
#         # mark all ch as False, update to True if it's contained in the word 
#         buckets = [False] * n
        
#         r = 0
#         for l in range(n):
#             for w in words:
#                 # if s[l:] starts with w
#                 if s.startswith(w,l):
#                     # find/update the end, so the range [l,r) need to be updated to True
#                     r = max(r,l+len(w))
#             # update the buckets for [l,r) to True
#             for i in range(l,r):
#                 buckets[i] = True
            
#         res = ''

#         for i in range(n):
#             # if the first ch is marked as True OR prev ch is False and cur is True 
#             if (i == 0 and buckets[i]) or (i > 0 and buckets[i] and not buckets[i-1]):
#                 res += '<b>'
#             res += s[i]
#             # if the last ch is marked as True OR next is False and cur is True 
#             if (i == n-1 and buckets[i]) or (i < n-1 and buckets[i] and not buckets[i+1]):
#                 res += '</b>'
        
#         return res 
                    
        
        
        
        
        
        
        
        
        
   
            
            
                
        
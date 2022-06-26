class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        buckets = [False] * n
        
        r = 0
        for l in range(n):
            for w in words:
                if s.startswith(w,l):
                    r = max(r,l+len(w))
            for i in range(l,r):
                buckets[i] = True
            
        res = ''

        for i in range(n):
            if (i == 0 and buckets[i]) or (i > 0 and buckets[i] and not buckets[i-1]):
                res += '<b>'
            res += s[i]
            if (i == n-1 and buckets[i]) or (i < n-1 and buckets[i] and not buckets[i+1]):
                res += '</b>'
        
        return res 
                    
        
        
        
        
        
        
        
        
        
   
            
            
                
        
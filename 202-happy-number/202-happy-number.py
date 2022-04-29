class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            total = 0
            
            for d in str(n):
                total += int(d) **2
            
            n = total
            
        return n == 1
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#       seen = set()

#       while n not in seen:

#         seen.add(n)
#         n = sum(int(a)**2 for a in str(n))

#       return n == 1
        
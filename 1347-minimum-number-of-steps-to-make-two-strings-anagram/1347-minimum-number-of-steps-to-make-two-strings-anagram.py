class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        count = Counter(s)
        
        for ch in t:
            if ch in count and count[ch]:
                count[ch] -= 1
        
        return sum(count.values())
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         steps = 0
#         d = dict()
        
#         for ch in s:
#             d[ch] = d.get(ch, 0) + 1
        
#         for ch in t:
#             if ch in d and d[ch]:
#                 d[ch] -=1
#             else:
#                 steps +=1
                
#         return steps
            
            
        
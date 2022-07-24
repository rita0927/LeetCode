class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = hour%12 * 30 + minutes/60 *30
        m = minutes*6
        
        diff = abs(h-m)
        return min(diff, 360-diff)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         h = hour%12 * 30 + minutes/60*30
#         diff = abs(h - minutes*6)
#         return min(diff, 360-diff)
        
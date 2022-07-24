class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        res = 0
        
        for n in nums:
            if n-k in d:
                res += d[n-k]
            if n+k in d:
                res += d[n+k]
            d[n] += 1
        return res 
        
        
            
        
        
        
        
        
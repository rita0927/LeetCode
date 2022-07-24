class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        res = 0
        count = Counter(nums)
        
        for n in count:
            if k > 0 and n+k in count:
                res += 1
            elif k == 0 and count[n] > 1:
                res +=1
        
        return res 
            
        
        
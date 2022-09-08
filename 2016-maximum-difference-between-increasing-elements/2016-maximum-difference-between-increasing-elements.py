class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        min_val = float('inf')
        res = 0
        for n in nums:
            min_val = min(min_val, n)
            res = max(res, n-min_val)
        
        return res if res !=0 else -1
        
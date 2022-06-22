class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        d = {}
        prefix = 0
        res = 0
        
        for i in range(len(nums)):
            prefix += nums[i]
            
            if prefix == k:
                res = i + 1
            
            if (prefix - k) in d:
                res = max(res, i - d[prefix - k])
            
            if prefix not in d:
                d[prefix] = i
                
        return res 
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         indices= {}
#         prefix = 0
#         res = 0
        
#         for i, n in enumerate(nums):
            
#             prefix +=n
            
#             if prefix == k:
#                 res = i + 1
            
#             if (prefix - k) in indices:
#                 res = max(res, i -indices[prefix-k])
            
#             if prefix not in indices:
#                 indices[prefix] = i
#         return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
        
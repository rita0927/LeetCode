class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        indices= {}
        prefix = 0
        res = 0
        
        for i, n in enumerate(nums):
            
            prefix +=n
            
            if prefix == k:
                res = i + 1
            
            if (prefix - k) in indices:
                res = max(res, i -indices[prefix-k])
            
            if prefix not in indices:
                indices[prefix] = i
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = 0
#         pre = 0
#         d = {}
        
#         for i, num in enumerate(nums):
            
#             pre += num
            
#             if pre == k:
#                 res=i+1
            
#             if pre - k in d:
#                 res = max(res, i-d[pre-k])
          
#             if pre not in d:
#                 d[pre] = i
            
#         return res 
            
            
        
        
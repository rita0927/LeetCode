class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if max(nums) < 0:
            return max(nums)
        
        local_max = 0
        global_max = 0
        
        for n in nums:
            local_max = max(local_max + n, 0)
            global_max = max(global_max, local_max)
        
        return global_max 
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         global_max= local_max= nums[0]
        
#         for n in nums[1:]:
#             # whether to abandon the previous local_max
#             local_max = max(n, local_max + n)
#             global_max = max(global_max, local_max)
            
#         return global_max 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if max(nums) < 0:
#             return max(nums)
        
#         local_max = 0
#         global_max = 0
        
#         for n in nums:
#             local_max = max(0, local_max + n)
#             global_max = max(global_max, local_max)
        
#         return global_max 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if max(nums) < 0:
#             return max(nums)
        
        
#         res = float('-inf')
#         temp = 0 
        
#         for i in range(len(nums)):
#             if temp + nums[i] <0:
#                 temp = 0 
#             else:
#                 temp += nums[i]
#             res = max([res, temp, nums[i]])
        
#         return res 
        
        

        
        
        
        
        
        
        
        
      
        

#         if max(nums) < 0:
#             return max(nums)

#         local_max, global_max = 0, 0
#         for num in nums:
#             local_max = max(0, local_max + num)
#             global_max = max(global_max, local_max)
#         return global_max
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        
        localMax, globalMax = 0, 0
        
        for num in nums:
            localMax = max(0, localMax + num)
            globalMax = max(globalMax, localMax)
        return globalMax 
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         if max(nums) < 0:
#             return max(nums)

#         local_max, global_max = 0, 0
#         for num in nums:
#             local_max = max(0, local_max + num)
#             global_max = max(global_max, local_max)
#         return global_max
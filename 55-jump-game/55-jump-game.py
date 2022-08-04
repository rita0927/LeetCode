class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_jump = 0
        
        for i, n in enumerate(nums):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i+n)
        return True 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         max_index = 0

#         for i in range(len(nums)):
#             if i > max_index:
#                 return False
#             cur = i + nums[i]
#             max_index = max(max_index, cur)

#         return max_index >= len(nums) - 1
        
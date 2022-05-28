class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0 
        p2 = len(nums) - 1
        cur = 0
        
        while cur <= p2:
            # index <= cur are sorted, no need to verify nums[cur] after the replacement
            if nums[cur] == 0:
                nums[p0], nums[cur] = nums[cur], nums[p0]
                p0+=1
                cur+=1
            # replaced nums[cur] is not verified, can't increase cur
            elif nums[cur] == 2:
                nums[p2], nums[cur] = nums[cur], nums[p2]
                p2 -=1
            else:
                cur += 1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         p0 = -1
#         p2 = len(nums)
#         cur = 0
        
#         while cur < p2:
#             if nums[cur] == 1:
#                 cur += 1
#             elif nums[cur] == 2:
#                 p2 -=1
#                 nums[p2], nums[cur] = nums[cur], nums[p2]
#             else:
#                 p0 += 1
#                 nums[p0], nums[cur] = nums[cur], nums[p0]
#                 cur += 1
                
        
        
    
        
 
        
        
        
        
        
        
        
        
        
        
        
#         zero = -1
#         two = len(nums)

#         i = 0

#         while i < two:
#             if nums[i] == 1:
#                 i += 1

#             elif nums[i] == 2:
#                 two -= 1
#                 nums[i], nums[two] = nums[two], nums[i]

#             else:
#                 zero += 1
#                 nums[i], nums[zero] = nums[zero], nums[i]
#                 i += 1
        
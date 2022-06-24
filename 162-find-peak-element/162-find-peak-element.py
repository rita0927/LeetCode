class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = -1
        r = len(nums)
        
        while l + 1 != r:
            mid = (l+r)//2
            
            if mid-1 >= 0 and nums[mid] <= nums[mid-1]:
                r = mid
            else:
                l = mid
        
        return l
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l = -1
#         r = len(nums)
        
#         while l + 1 != r:
#             mid = (l+r)//2
            

#             if mid + 1 < len(nums) and nums[mid] <= nums[mid + 1]:
#                 l = mid
#             else:
#                 r = mid
        
#         return r 
        
        
        
 
        
        
        
        
        
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             mid = left + (right - left) // 2
#             if nums[mid] < nums[mid + 1]:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left 
        
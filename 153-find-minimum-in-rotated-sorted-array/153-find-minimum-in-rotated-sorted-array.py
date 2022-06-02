class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        if nums[l] <= nums[r]:
            return nums[0]
        
        while l < r:
            mid = l + (r-l)//2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
        return nums[r] 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l, r = 0, len(nums) - 1
#         if nums[l] <= nums[r]:
#             return nums[0]

#         while l < r:
#             mid = (l + r) // 2
#             if nums[mid] >= nums[r]:
#                 l = mid + 1
#             else:
#                 r = mid 

#         return nums[r]
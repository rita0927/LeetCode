class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        
        l = 0
        r = len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            if nums[l] ** 2 > nums[r] ** 2:
                res[i] = nums[l] ** 2
                l += 1
            else:
                res[i] = nums[r] ** 2
                r -= 1
        return res 
        
    

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = [0] * len(nums)
#         l = 0
#         r = len(nums)-1
        
#         for i in range(len(nums)-1, -1, -1):
#             if nums[l] ** 2 > nums[r] ** 2:
#                 res[i] = nums[l]**2
#                 l +=1 
#             else:
#                 res[i] = nums[r]**2
#                 r -= 1
#         return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # return sorted([i**2 for i in nums])
        
        
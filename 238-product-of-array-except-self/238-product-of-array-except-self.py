class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        right = 1
        
        for j in range(len(nums) - 1, -1, -1):
            res[j] *=right
            right*=nums[j]
        
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n), O(n)
#         left = [1] * len(nums)
#         right = [1] * len(nums)
#         res = [1] * len(nums)
        
#         for i in range(1, len(nums)):
#             left[i] = left[i-1] * nums[i-1]
        
#         for j in range(len(nums)-2, -1, -1):
#             right[j] = right[j+1] * nums[j+1]
            
#         res = [left[i] * right[i] for i in range(len(nums))]
#         return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = [1] * len(nums)
        
#         for i in range(1, len(nums)):
#             res[i]= res[i-1] * nums[i-1]
        
#         right = 1
#         for j in range(len(nums) - 1, -1, -1):
#             res[j] *= right
#             right*=nums[j]
#         return res 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#       res = [1] * len(nums)

#       for i in range(1, len(nums)):
#         res[i] = res[i-1] * nums[i-1]

#       right = 1
#       for i in range(len(nums) -1, -1, -1):
#         res[i] = res[i] * right
#         right = right * nums[i]
#       return res
        
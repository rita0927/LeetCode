class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(nums) > len(set(nums))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         numsSet = set(nums)

#         return len(nums) != len(numsSet)
        
        
        
#       nums.sort()
#       curr = nums[0]
#       for i in range(1, len(nums)):

#         if nums[i]^ curr== 0:
#           return True
#         curr = nums[i]
#       return False
        
        
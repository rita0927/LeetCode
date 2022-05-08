class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        # base case
        if len(nums) == 1:
            return [nums.copy()]
            return [nums[:]]
        
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            
            res.extend(perms)
            nums.append(n)
            
        return res
            
        
            
    
    
             
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         result = []

#         def backtrack(result, tempList, nums):
#             if len(tempList) == len(nums):
#                 result.append(copy.copy(tempList))

#             for i in range(len(nums)):
#                 if nums[i] in tempList:
#                     continue
#                 tempList.append(nums[i])
#                 backtrack(result, tempList, nums)
#                 tempList.pop()

#             return result

#         return backtrack(result, [], nums)
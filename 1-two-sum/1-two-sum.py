class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        
        for i in range(len(nums)):
            if (target - nums[i]) in dic:
                return [i, dic[target - nums[i]]]
            dic[nums[i]] = i
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
           
        
        
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]

# O(n^2), O(1)
        
#         dic = {}
#         for i in range(len(nums)):
#             dic[nums[i]]= i 
            
#         for i in range(len(nums)):
#             complement = target-nums[i]
#             if complement in dic and i!=dic[complement]:
#                 return [i, dic[complement]]
            
# O(n), O(n)            
   
    
#         hash = {}
#         for i in range(len(nums)):
#             complement = target -nums[i]
#             if complement in hash:
#                 return [i, hash[complement]]
#             # avoid having the comlement being the nums[i] itself
#             hash[nums[i]] = i
            
# # O(n), O(n)    
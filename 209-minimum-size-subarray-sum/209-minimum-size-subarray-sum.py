class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = float('inf') 
        l = 0
        total = 0 
        for r in range(len(nums)):
            total += nums[r]
            
            while total >= target:
                res = min(res, r-l+1)
                total -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0 
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n^3)    ETL
#         res = float('inf')
        
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):

#                 total = sum(nums[i:j+1])
                    
#                 if total >= target:
#                     res = min(res, j-i+1)
        
#         return res if res != float('inf') else 0
                
                
      
        
        
        
    
        
        
        
#         # O(n), O(1)
        
#         total = 0
#         res = float('inf')
#         l = 0
        
        
#         for r in range(len(nums)):
#             total +=nums[r]
            
            
#             while total >= target:
#                 res = min(res, (r- l + 1))
#                 total -=nums[l]
#                 l+=1
                
#         return res if res != float('inf') else 0
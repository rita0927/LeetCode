class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()
        
        for i in range(1, len(nums)-1):
            l = i-1
            r = i+1
            
            while l >= 0 and r < len(nums):
                total = nums[i] + nums[l] + nums[r]
                
                if total > 0:
                    l -= 1
                elif total < 0:
                    r += 1
                else:
                    res.add((nums[l], nums[i], nums[r]))
                    l -= 1
                    r += 1
        return res 
        

        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n^2), O(logn) due to the sorting
        
        
#         res = set()
#         nums.sort()
        
#         for i in range(1, len(nums) - 1):
            
#             l = i - 1
#             r = i + 1
            
#             while l >= 0 and r < len(nums):
                
#                 total = nums[l] + nums[i] + nums[r]
                
#                 if total >0:
#                     l -=1
#                 elif total < 0:
#                     r += 1
#                 else:
#                     res.add((nums[l], nums[i], nums[r]))
#                     l-=1
#                     r+=1
                    
#         return res 
                
            
            
            
        
        
        

        
            

      
        
        
#         res = set()
#         nums.sort()
        
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 break
#             if i> 0 and nums[i] == nums[i-1]:
#                 continue
#             l, r = i + 1, len(nums)-1
#             while l < r:
#                 tol = nums[i] + nums[l] + nums[r]
#                 if tol > 0:
#                     r -=1
#                 elif tol < 0:
#                     l +=1
#                 else: 
#                     res.add((nums[i], nums[l], nums[r]))
#                     l +=1
#                     r-=1
#         return res
                
                
# O(n^2), O(n)
# Space complexity depens on the sort, which can take from O(logn) to O(n) 
        
      
        
        
        
        
        
        
        
        
        
        
        
#         if len(nums) <3:
#             return []
        
#         res = set()
#         nums.sort()  
        
#         for i in range(1, len(nums)-1):
                
#             l, r = i-1, i+1
            
#             while l>=0 and r <len(nums):
#                 sum = nums[l] + nums[i] + nums[r] 
#                 if sum > 0:
#                     l-=1
#                 elif sum < 0:
#                     r +=1
#                 else:
#                     res.add((nums[l], nums[i], nums[r]))
#                     l-=1
#                     r+=1
#         return res
                    
        
        
      
        
        
        
        
        
        
#         res = set()
#         nums.sort()
#         for i, num1 in enumerate(nums):
#             if i > 0 and num1 == nums[i - 1]:
#                 continue

#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 sum = num1 + nums[l] + nums[r]
#                 if sum > 0:
#                     r -= 1
#                 elif sum < 0:
#                     l += 1
#                 else:
#                     res.add((num1, nums[l], nums[r]))
#                     l+=1
#                     r-=1
#         return res
        
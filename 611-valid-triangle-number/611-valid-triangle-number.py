class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0 

        for i in range(len(nums)-1, 1,-1):
            l = 0
            r = i-1
            
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += r-l
                    r -= 1
                else:
                    l += 1
        return res 
            
            
        
 
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n^2), O(logn) due to the sort 
        
#         # optional 
#         if len(nums) < 3:
#             return 0
        
#         res = 0
#         nums.sort(reverse = True)
#         for a in range(len(nums) - 2):
#             b = a + 1
#             c = len(nums) - 1
            
#             while b < c:
#                 if nums[b] + nums[c] > nums[a]:
#                     res += c - b
#                     b += 1
#                 else:
#                     c -= 1
#         return res 
        
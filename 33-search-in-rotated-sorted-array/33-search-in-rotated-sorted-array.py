class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = -1
        r = len(nums) 
        
        while l+1 != r:   
            mid = (l+r)//2

            if nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    r = mid
                else: 
                    l = mid 
                    
            elif nums[mid] <= nums[len(nums) -1]:
                if nums[mid] <= target <= nums[len(nums) -1]:
                    l = mid 
                else:
                    r = mid 
        return l if nums[l] == target else -1
                    


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         l = 0
#         r = len(nums) -1
        
        
#         while l <= r:
#             mid = l + (r-l)//2  
            
#             if nums[mid] == target:
#                 return mid
            
#             if nums[mid] >= nums[l]:
#                 if nums[l] <= target < nums[mid]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1

#             elif nums[mid] <= nums[r]:
                
#                 if nums[mid] < target <= nums[r]:
#                     l = mid + 1
                
#                 else:
#                     r = mid - 1
            
#         return -1

        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l = 0
#         r = len(nums)-1
        
        
#         while l<= r:
#             mid = l + (r-l)//2
            
#             if nums[mid] == target:
#                 return mid
            
#             elif nums[mid] >= nums[l]:
#                 if nums[l] <= target < nums[mid]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             elif nums[mid] <= nums[r]:
#                 if nums[mid] < target <= nums[r]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#         return -1
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not nums:
#             return -1

#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = (l + r) // 2

#             if nums[mid] == target:
#                 return mid
#             elif nums[l] == target:
#                 return l
#             elif nums[r] == target:
#                 return r

#             if nums[mid] > nums[l]:
#                 if nums[l] < target < nums[mid]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             else:
#                 if nums[mid] < target < nums[r]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#         return -1
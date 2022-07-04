class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:   
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else: 
                    l = mid + 1

            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
                    


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

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
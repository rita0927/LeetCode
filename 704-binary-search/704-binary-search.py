class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l=-1
        r=len(nums)
        while l+1!=r:
            mid=(l+r)//2
            
            if nums[mid]<=target:
                l=mid
            else:
                r=mid
        return l if nums[l]==target else -1



    
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l = -1
#         r = len(nums)

#         while l+1 != r:
#             mid = (l+r)//2
            
#             if nums[mid] <= target:
#                 l = mid
#             else:
#                 r = mid
#         return l if nums[l] == target else -1
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l = -1
#         r = len(nums)
        
#         while l + 1 != r:
#             mid = (l+r)//2
            
#             if nums[mid] <=target:
#                 l = mid
#             else:
#                 r = mid
            
#         return l if nums[l] == target else -1
        
        
        
        
        
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] > target:
#                 r = mid - 1
#             elif nums[mid] < target:
#                 l = mid + 1
#             else:
#                 return mid
#         return -1
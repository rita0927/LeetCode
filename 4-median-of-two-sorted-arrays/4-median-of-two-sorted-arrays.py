class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        mid = length//2
        odd = length%2
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l = 0 
        r = len(nums1) - 1
        
        while True:
            mid1 = (l + r)//2
            mid2 = mid - mid1 - 2
            
            left1 = nums1[mid1] if mid1 >=0 else float('-inf')
            right1 = nums1[mid1 + 1] if (mid1 + 1) < len(nums1) else float('inf')
            left2 = nums2[mid2] if mid2 >=0 else float('-inf')
            right2 = nums2[mid2 + 1] if mid2 + 1 <len(nums2) else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                if odd:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2))/2
            
            elif left1 > right2:
                r = mid1 - 1
            else:
                l = mid1 + 1
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         #O(log(min(m,n))), O(1)

#         length = len(nums1) + len(nums2)
#         mid = length//2
#         odd = length % 2
        
#         if len(nums1) > len(nums2):
#             nums1, nums2 = nums2, nums1
            
#         l = 0
#         r = len(nums1) - 1
        
#         while True:
#             mid1 = (l+r)//2
            
#             # mid index of b, b_mid + 1 + a_mid + 1 = mid
#             mid2 = mid - mid1 - 2  
            
#             left1 = nums1[mid1] if mid1 >=0 else float('-inf')
#             right1 = nums1[mid1 + 1] if mid1 + 1 < len(nums1) else float('inf')
#             left2 = nums2[mid2] if mid2 >=0 else float('-inf')
#             right2 = nums2[mid2 + 1] if mid2 + 1 < len(nums2) else float('inf')
            
#             if left1<=right2 and left2 <=right1:
#                 if odd:
#                     return min(right1, right2)
#                 return (max(left1, left2) + min(right1, right2))/2
            
#             if left1 >right2:
#                 r = mid1 - 1
                
#             # left2 > right1
#             else:  
#                 l = mid1 + 1
                
                
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(nums1) > len(nums2):
        #     return self.findMedianSortedArrays(nums2, nums1)
        # int_min, int_max = -(2 ** 64), 2 ** 64
        # merged_len = len(nums1) + len(nums2)
        # start1, end1 = 0, len(nums1)
        # while start1 <= end1:
        #     cut1 = (start1 + end1) // 2
        #     cut2 = (merged_len + 1) // 2 - cut1
        #     l1 = nums1[cut1 - 1] if cut1 > 0 else int_min
        #     l2 = nums2[cut2 - 1] if cut2 > 0 else int_min
        #     r1 = nums1[cut1] if cut1 < len(nums1) else int_max
        #     r2 = nums2[cut2] if cut2 < len(nums2) else int_max
        #     if l1 > r2:
        #         end1 = cut1 - 1
        #     elif l2 > r1:
        #         start1 = cut1 + 1
        #     else:
        #         if merged_len % 2 == 0:
        #             return (max(l1, l2) + min(r1, r2)) / 2
        #         else:
        #             return max(l1, l2)
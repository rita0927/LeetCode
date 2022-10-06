class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """

        i1=m-1
        i2=n-1
        
        for i in range(m+n-1,-1,-1):
            if i2<0:
                break
            if i1>=0 and nums1[i1]>nums2[i2]:
                nums1[i]=nums1[i1]
                i1-=1
            else:
                nums1[i]=nums2[i2]
                i2-=1
        return nums1
            
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#     # O(m + n), O(1)
        
#         p1= m-1
#         p2 = n-1
        
        
#         for p in range(m + n - 1, -1, -1):
#             if p2 < 0:
#                 break
#             if p1 >=0 and nums1[p1] > nums2[p2]:
#                 nums1[p] = nums1[p1]
#                 p1-=1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2-=1
            
            
            
            
            
            
# O((m+n)*log(m+n))
# O(n)

#         for i in range(n):
#             nums1[i + m] = nums2[i]
#         nums1.sort()
        
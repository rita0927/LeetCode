class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        res = 0
        
        while l < r:
            w = r - l 
            res = max(res, w * min(height[l], height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res 
            
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = 0
#         l = 0 
#         r = len(height) - 1
        
#         while l < r:
#             width = r - l 
#             res = max(res, min(height[l], height[r]) * width)
#             if height[l] < height[r]:
#                 l += 1
#             else:
#                 r -= 1
        
#         return res 
                


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

       
        
     
        
        
        
        
        
#         l = 0
#         r = len(height) - 1
#         area = 0
        
#         while l < r:
#             area = max(area, min(height[l],height[r]) * (r-l))
#             if height[l] < height[r]:
#                 l +=1
#             else: 
#                 r -=1
#         return area 


# O(n), O(1)
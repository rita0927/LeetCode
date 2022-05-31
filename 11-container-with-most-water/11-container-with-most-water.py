class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res = 0
        l = 0 
        r = len(height) - 1
        
        while l < r:
            width = r - l 
            res = max(res, min(height[l], height[r]) * width)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res 
                


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

       
        
     
        
        
        
        
        
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
class Solution:
    def trap(self, height: List[int]) -> int:
        
        peak = 0
        for i in range(len(height)):
            if height[i] > height[peak]:
                peak = i
                
        water = 0
        left = 0
        for i in range(peak):
            if height[i]>height[left]:
                left = i
            else:
                water += (height[left] - height[i])
            
        right = len(height) - 1
        for i in range(right, peak, -1):
            if height[i] > height[right]:
                right = i
            else:
                water += (height[right]-height[i])
        return water 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         peak = 0
#         for i in range(len(height)):
#             if height[i] > height[peak]:
#                 peak = i
#         leftMost = 0
#         water = 0
#         for i in range(peak):
#             if height[i] > leftMost:
#                 leftMost = height[i]
#             else:
#                 water = water + leftMost - height[i]
#         rightMost = 0

#         for i in range(len(height) - 1, peak, -1):
#             if height[i] > rightMost:
#                 rightMost = height[i]
#             else:
#                 water = water + rightMost - height[i]
#         return water
        
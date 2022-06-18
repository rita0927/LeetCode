class Solution:
    def trap(self, height: List[int]) -> int:
        
        peak = 0
        
        for i in range(len(height)):
            if height[i] >= height[peak]:
                peak = i
        res= 0
        l = height[0]
        for i in range(peak):
            if height[i] < l:
                res += l- height[i]
            else:
                l = height[i]
            
        r = height[-1]
        for i in range(len(height)-1, peak, -1):
            if height[i] < r:
                res += r - height[i]
            else:
                r = height[i]
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = 0
#         l = 0
#         r = len(height) - 1
#         l_max = height[l]
#         r_max = height[r]
        
#         while l < r:
            
#             if l_max < r_max:
#                 res += (l_max - height[l])
#                 l +=1
#                 l_max = max(l_max, height[l])
#             else:
#                 res += (r_max - height[r])
#                 r -=1
#                 r_max = max(r_max, height[r])
#         return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      # # O(N^2) ETL  
      #   res = 0
      #   for i in range(1,len(height)):
      #       cur = min(max(height[:i]), max(height[i:]))
      #       if (cur > height[i]):
      #           res += (cur - height[i])
      #   return res   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         peak = 0
#         for i in range(len(height)):
#             if height[i] > height[peak]:
#                 peak = i
                
#         water = 0
#         left = 0
#         for i in range(peak):
#             if height[i]>height[left]:
#                 left = i
#             else:
#                 water += (height[left] - height[i])
            
#         right = len(height) - 1
#         for i in range(right, peak, -1):
#             if height[i] > height[right]:
#                 right = i
#             else:
#                 water += (height[right]-height[i])
#         return water 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
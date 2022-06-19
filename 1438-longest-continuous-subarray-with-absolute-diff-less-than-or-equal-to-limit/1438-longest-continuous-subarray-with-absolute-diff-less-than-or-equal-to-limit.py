class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        max_stack = []
        min_stack = []
        res = 0
        l = 0
        
        for r in range(len(nums)):
            
            while max_stack and nums[r] > nums[max_stack[-1]]:
                max_stack.pop()
            max_stack.append(r)
            
            while min_stack and nums[r] < nums[min_stack[-1]]:
                min_stack.pop()
            min_stack.append(r)
            
            
            while nums[max_stack[0]] - nums[min_stack[0]] > limit:
                
                if max_stack[0] == l:
                    max_stack.pop(0)
                
                if min_stack[0] == l:
                    min_stack.pop(0)
                    
                l += 1
                
            res = max(res, r-l+1)
        return res 
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         maxQueue = deque()  
#         minQueue = deque()   
#         res = 0     
#         l = 0   
        
#         for r in range(len(nums)):
#             # maintain max values in current subarray
#             while maxQueue and nums[r] > maxQueue[-1]:
#                 maxQueue.pop()
#             maxQueue.append(nums[r])
            
#             # maintain min value in current subarray
#             while minQueue and nums[r] < minQueue[-1]:
#                 minQueue.pop()
#             minQueue.append(nums[r])
            
#             while maxQueue[0] - minQueue[0] >limit:
#                 # if the left pointer points to the max value
#                 # remove the max value before moving the left pointer to maintain a valid queue
#                 if maxQueue[0] == nums[l]:
#                     maxQueue.popleft()
                    
#                 # if the left pointer points to the min value
#                 if minQueue[0] == nums[l]:
#                     minQueue.popleft()
#                 l+=1
                
#             res = max(res, r - l + 1)
                                    
#         return res 
            
        
        
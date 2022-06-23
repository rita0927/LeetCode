class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        maxQ = deque()
        minQ = deque()
        res = 0
        l = 0
        
        for r in range(len(nums)):
            
            while maxQ and nums[r] > nums[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(r)
            
            while minQ and nums[r] < nums[minQ[-1]]:
                minQ.pop()
            minQ.append(r)
            
            while nums[maxQ[0]] - nums[minQ[0]] > limit:
                if l == maxQ[0]:
                    maxQ.popleft()
                if l == minQ[0]:
                    minQ.popleft()
                l+=1 
            
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
            
        
        
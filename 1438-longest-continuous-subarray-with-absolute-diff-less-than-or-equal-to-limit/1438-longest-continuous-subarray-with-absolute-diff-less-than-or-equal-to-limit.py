class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        maxQueue = deque()  
        minQueue = deque()   
        res = 0     
        l = 0   
        
        for r in range(len(nums)):
            while maxQueue and nums[r] > maxQueue[-1]:
                maxQueue.pop()
            maxQueue.append(nums[r])
            
            while minQueue and nums[r] < minQueue[-1]:
                minQueue.pop()
            minQueue.append(nums[r])
            
            while maxQueue[0] - minQueue[0] >limit:
                if maxQueue[0] == nums[l]:
                    maxQueue.popleft()
                if minQueue[0] == nums[l]:
                    minQueue.popleft()
                l+=1
            
            res = max(res, r - l + 1)
                                    
        return res 
            
        
        
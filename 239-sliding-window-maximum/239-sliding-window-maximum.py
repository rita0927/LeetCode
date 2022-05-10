class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l,r = 0, 0 
        queue = deque()
        
        while r < len(nums):
            
            while queue and nums[r] > queue[-1]:
                queue.pop()
            queue.append(nums[r])
            
            if r + 1>=k:
                res.append(queue[0])
                if nums[l] == queue[0]:
                    queue.popleft()
                l+=1
            r +=1
        return res 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # brute force 
#         # Time: O((n-k+1) * k) where k elements in each window
#         # Space: O(1)

#         res = []
#         for i in range(len(nums) - k + 1):
#             res.append(max(nums[i: i + k]))  
#         return res 
        
        
#         res = []
#         l,r = 0, 0 
#         queue = deque()
        
#         while r <len(nums):
            
#             while queue and nums[r] > nums[queue[-1]]:
#                 queue.pop()
#             queue.append(r)
            
#             if l > queue[0]:
#                 queue.popleft()
            
#             if r + 1>=k:
#                 res.append(nums[queue[0]])
#                 l +=1
#             r +=1
#         return res 
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
#         l,r = 0, 0
#         maxQueue = deque()
  
#         while r < len(nums):
#             while maxQueue and nums[r] >nums[maxQueue[-1]]:
#                 maxQueue.pop()
#             maxQueue.append(r)

#             if l > maxQueue[0]:
#                 maxQueue.popleft()
            
#             # append to the res when the right pointer >= window width - 1
#             if r + 1 >= k: 
#                 res.append(nums[maxQueue[0]])
#                 l+=1
#             r+=1
            
#         return res 
            
            
            
        
        
        
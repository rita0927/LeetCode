class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        res = []
        queue = deque()
        
        for r in range(len(nums)):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            
            if r + 1 >= k:
                res.append(nums[queue[0]])
                
                if queue[0] == l:
                    queue.popleft()
                l += 1
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
#         l = 0 
#         queue = deque()
        
#         for r in range(len(nums)):
            
#             while queue and nums[queue[-1]] < nums[r]:
#                 queue.pop()
#             queue.append(r)
            
#             if r + 1 >=k:
#                 res.append(nums[queue[0]])
                
#                 if l == queue[0]:
#                     queue.popleft()
#                 l+=1
                
#         return res 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # Brute Force: O(nk), O(n-k+1) for output 
#         return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]
        
        
   
        
        
        
        
# # O(n), O(n) where O(n-k+1) for output and O(k) for stack
#         res = []
#         stack = []
#         l = 0
        
#         for r in range(len(nums)):
            
#             while stack and nums[stack[-1]] < nums[r]:
#                 stack.pop()
#             stack.append(r)
            
#             if (r-l+1) >= k:
#                 res.append(nums[stack[0]])
                
#                 if stack[0] == l:
#                     stack.pop(0)
#                 l+=1
#         return res 
                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
#         l,r = 0, 0 
#         queue = deque()
        
#         while r < len(nums):
            
#             while queue and nums[r] > queue[-1]:
#                 queue.pop()
#             queue.append(nums[r])
            
#             # start append to the res once reaches window width
#             if r + 1>=k:
#                 res.append(queue[0])
                
#                 # adjust the range of queue beofre moving the left pointer 
#                 if nums[l] == queue[0]:
#                     queue.popleft()
#                 l+=1
#             r +=1
#         return res 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
            
            
            
        
        
        
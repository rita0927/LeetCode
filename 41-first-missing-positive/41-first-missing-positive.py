class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for i in range(n):
            
            while nums[i] in range(1, n+1) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i] -1]
        
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
                

        

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n) for & while. While loop will place one element into the correct index every time. 
        
#         n = len(nums)
#         for i in range(n):
#             # put nums[i] to the correct index (nums[i]-1) if nums[i] is between 1 and n inclusive
#             # the min res is 1, and the max res is len(nums)+1 (when all previous positives are provided)
#             # need while loop for continuous swap
#             # a smaller number may be swapped into the index i and making it wrongly positioned
#             # ex. [-1, 4, 3, 1], i = 1, after swapping 4 and 1, we will have [-1, 1, 3, 4]. 4 is correctly positioned but 1 is wrongly placed, we still need to swap it with -1, so the array becomes [1, -1, 3, 4], which is in correct order.
                
#             while nums[i] in range(1, n+1) and nums[nums[i]-1] != nums[i]:
#                 nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
#         # all the integers ([1,len(nums)]) have been put to the correct index
#         # if the index i is not occupied by i+1, this's a missing positive
#         for i in range(n):
#             if nums[i] != i+1:
#                 return i+1
#         return n+1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         nums.append(0)
#         N = len(nums)

#         for i in range(N):
#             if nums[i] < 0 or nums[i] > N:
#                 nums[i] = 0
#         temp = nums[0]
#         for i in range(N):
#             if nums[i] > 0:
#                 nums[nums[i] % N - 1] += N

#         if nums[0] == temp:
#             return 1
#         for i in range(N):
#             if nums[i] // N == 0:
#                 return i + 1

#         return N
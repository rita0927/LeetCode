class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            
            while nums[i] in range(1, n+1) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
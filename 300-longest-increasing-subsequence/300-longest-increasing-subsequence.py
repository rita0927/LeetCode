class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        N = len(nums)
        dp = [1] * N
        
        for i in range(1,N):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n^2), O(n)
        
#         # find all the previous num less than current num, and take the max dp[num] + 1 
#         N = len(nums)
#         # use dp to record max lenth at each index
#         dp= [1] * N
        
#         # iterating over the dp
#         for i in range(1,N):
#             # iterating over the previous num before nums[i]
#             for j in range(i):
#                 # update dp[i] when the nums[j] less than nums[i]
#                 if nums[j] < nums[i]:
#                     # use the result from dp[j] and include the new element nums[i]
#                     dp[i] = max(dp[i], dp[j] + 1)
                    
#         return max(dp)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         N = len(nums)
#         dp = [1] * N

#         for n in range(N):
#             for i in range(n):
#                 if nums[i] < nums[n]:
#                     dp[n] = max(dp[n], dp[i] + 1)
#         return max(dp) 
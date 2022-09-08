class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        return dp[-1]
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # to maxmize the amt, skip the adjacent house. Either rob index 0,2,4.. or rob 1,3,5...
#         # if skip the house -> take the previous dp
#         # if rob the house -> take the dp[i-2] + nums[i]
#         # compare two amount, and record the max as dp[i]
        
#         # if only 1 or 2 nums, take the max
#         if len(nums) < 3:
#             return max(nums)
        
#         dp = [0] * len(nums)
        
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])
        
#         for i in range(2, len(nums)):
#             # either the previous dp, or the skip the previous dp, take the sum of the i-2 and current num
#             dp[i] = max(dp[i-1], dp[i-2] + nums[i])
#         # return the last dp 
#         return dp[-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(nums) < 3:
#             return max(nums)

#         dp = [0] * len(nums)

#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])

#         for i in range(2, len(nums)):
#             dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
#         return dp[-1]
class Solution:
    def climbStairs(self, n: int) -> int:
        
        two = 1
        one = 1
        cur = 1
        for i in range(2,n+1):
            cur = two + one 
            two = one
            one = cur 
        
        return cur 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n), O(n)
#         dp = [0] * (n+1)
#         dp[0] = 1
#         dp[1] = 1
        
#         for i in range(2,n+1):
#             dp[i] = dp[i-1]+dp[i-2]
        
#         return dp[n]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # prev, cur = 0, 1
        # for i in range(n):
        #     prev, cur = cur, prev + cur
        # return cur
        
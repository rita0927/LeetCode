class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for a in range(1,amount+1):
            for c in coins:
                if a >=c:
                    dp[a] = min(dp[a], dp[a-c] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
        
        

            
        


        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(S*n) where S is the amount, n is denomination count 
#         # O(S)
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0
        
#         for a in range(1, amount + 1):
#             for c in coins:
#                 if a>=c:
#                     # dp[a-c] + 1, dp[a-c] to get the dp from cache, 1 is for the current coin c
#                     # get the min from available combinations (compare all coins combination and the default dp[a])
#                     dp[a] = min(dp[a], dp[a-c]+1)
            
#         return dp[amount] if dp[amount] != float('inf') else -1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(S*N) where S is the amount, N is denomination count
#         # O(S)
        
#         memo = {}
        
#         def helper(balance):
#             if balance < 0: return -1
#             if balance == 0: return 0
#             if balance in memo:
#                 return memo[balance]
            
#             min_count = float('inf')
#             for c in coins:
#                 count = helper(balance - c)
#                 if count == -1: continue
#                 min_count = min(min_count, count + 1)
#             memo[balance] = min_count if min_count != float('inf') else -1
#             return memo[balance]
        
#         return helper(amount)
        

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dp=[0]*(amount+1)
        # dp[0] = 1
        # for coin in coins:
        #       for i in range(1, amount+1):
        #             if i - coin >=0:
        #                   dp[i] += dp[i-coin]
        # return dp[-1]

        
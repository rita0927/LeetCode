class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[1] * n] * m
        
        for r in range(1, m):
            for c in range(1,n):
                res[r][c] = res[r-1][c] + res[r][c-1]
        
        return res[m-1][n-1]
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#        #  O(M*N), O(M*N)
#         dp = [[1] * n] * m
        
#         for r in range(1,m):
#             for c in range(1,n):
#                 dp[r][c] = dp[r-1][c] + dp[r][c-1]
#         return dp[m-1][n-1]
        
        
        
        
    
        
#         res = [[1] * n] * m
#         for row in range(1, m):
#             for col in range(1, n):
#                 res[row][col] = res[row - 1][col] + res[row][col - 1]

#         return res[m - 1][n - 1]
        
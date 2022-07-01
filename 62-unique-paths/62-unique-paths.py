class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1] * n for _ in range(m)]
        
        for r in range(1,m):
            for c in range(1,n):
                matrix[r][c] = matrix[r-1][c] + matrix[r][c-1]
        
        return matrix[m-1][n-1]

        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
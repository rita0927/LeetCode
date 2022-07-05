class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for r in range(n):
            mid = n//2
            for c in range(mid):
                matrix[r][c], matrix[r][-c-1] = matrix[r][-c-1], matrix[r][c]
        
        return matrix 

        
                


                
                
                
        
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#  O(M) M is the number of cells. Two steps, each step we only move each cell once  
# O(1)

        
#         n = len(matrix)
#         matrix.reverse()
        
#         for i in range(n):
#             for j in range(i + 1,n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
       
        
        
#         n = len(matrix)
#         # transpose 
#         for i in range(n):
#             for j in range(i+1, n): 
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
#         # reflect 
#         for i in range(n):
#             for j in range(n//2):          
#                 matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
        
        
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         matrix.reverse();
        
#         for r in range(len(matrix)):
#             for c in range(r):
#                 matrix[r][c], matrix[c][r]= matrix[c][r], matrix[r][c]
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # matrix.reverse()
        # for r in range(len(matrix)):
        #     for c in range(r):
        #         matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
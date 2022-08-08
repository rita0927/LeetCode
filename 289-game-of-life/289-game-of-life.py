class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dir = [[-1,0], [1,0], [0,-1], [0,1], [-1,-1], [-1,1], [1,-1], [1,1]]
        
        for r in range(m):
            for c in range(n):
                lives = 0
                
                for x,y in dir:
                    nr = x + r
                    nc = y + c
                    
                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                        lives += 1
                        
                if board[r][c] == 1:
                    if lives < 2 or lives > 3:
                        board[r][c] = -1
                elif board[r][c] == 0:
                    if lives == 3:
                        board[r][c] = 2
        
        for r in range(m):
            for c in range(n):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0

 

                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m = len(board)
#         n = len(board[0])

#         for i in range(m):
#           for j in range(n):
#             lives = 0
#             for y in range(max(0, i-1), min(m, i+2)):
#               for x in range(max(0, j-1), min(n, j+2)):
#                 lives += board[y][x] & 1
#             if (lives ==3 or lives -board[i][j] == 3):
#               board[i][j] |=0b10

#         for i in range(m):
#           for j in range(n):
#             board[i][j] >>=1
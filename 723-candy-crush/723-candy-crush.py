class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board)
        n = len(board[0])
        toCrush = False
        
        for r in range(m):
            for c in range(n-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    toCrush = True
        
        for c in range(n):
            for r in range(m-2):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    toCrush = True
        

        for c in range(n):
            p = m-1
            for r in range(m-1, -1, -1):
                if board[r][c] > 0:
                    board[p][c] = board[r][c]
                    p -= 1
            for r in range(p, -1, -1):
                board[r][c] = 0
        
        return self.candyCrush(board) if toCrush else board 
            
                  
                
                
        
            
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# O(R*C) ^ 2 because each recursion call will scan the board 3 times (3*R*C). If we only crush 3 candies each time (min candies to triger the recursion),  the board size R*C needs to be divided by 3 to get the recursions/calls we need. That is, we need R*C/3 recursions to eliminate all the candies. Multiply (3*R*C) for each recursion and max calls (R*C/3), the final time complexity is (R*C) ^2        

# O(1)
        
#         # O((m*n) ^ 2), O(1) edit the board in place 
#         m = len(board)
#         n = len(board[0])
#         toCrush = False 
        
#         for r in range(m):
#             for c in range(n-2):

#                # use abs to cover previous marked cell, e.g. -5,-5,-5,5,5
#                 if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:
#                     board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
#                     toCrush = True
        
#         for c in range(n):
#             for r in range(m-2):
#                 if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
#                     board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
#                     toCrush = True 
        
        
        
#         for c in range(n):
            
#             # starting index for the positive num in each col 
#             # index > p is replaced with new num
#             # index <= p is updated to 0
#             p = m - 1
            
#             for r in range(m-1, -1, -1):
#                 if board[r][c] > 0:
#                     board[p][c] = board[r][c]
#                     p -= 1
            
#             for r in range(p, -1, -1):
#                 board[r][c] = 0 
                
#         return self.candyCrush(board) if toCrush else board 
                
                
        
        
        
        
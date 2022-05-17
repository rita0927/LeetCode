class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dir = [[-1,0], [1,0], [0,-1], [0,1]]      
        
        
        def backtrack(r,c,index):
            if index == len(word):
                return True
            
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
                return False
            
            board[r][c] = '#'
            for x,y in dir:
                nr = x + r
                nc = y + c
                
                if backtrack(nr, nc, index + 1):
                    return True
            board[r][c] = word[index]
            return False
        
        for r in range(m):
            for c in range(n):
                if backtrack(r,c,0):
                    return True
        return False 
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m = len(board)
#         n = len(board[0])
#         dir = [[-1,0], [1,0], [0,-1], [0,1]]
        
#         def backtrack(r,c,suffix):
            
#             if not suffix:
#                 return True

            # doing the boundary check within the function would allow us to reach the bottom case
            # example: [["a"]], "a"
        
#             if r< 0 or r >=m or c < 0 or c >=n or suffix[0] != board[r][c]:
#                 return False
            
#             board[r][c] = '#'
#             for x,y in dir:
#                 nr = x + r
#                 nc = y + c
#                 if backtrack(nr, nc, suffix[1:]):
#                     return True
#             board[r][c] = suffix[0]
#             return False
                   
        
#         for r in range(m):
#             for c in range(n):
#                 if backtrack(r,c,word):
#                     return True
#         return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m = len(board)
#         n = len(board[0])
#         dir = [[-1,0], [1,0], [0,-1], [0,1]]
        
        
#         def backtrack(index, r,c):
#             if index == len(word):
#                 return True
            
#             if r < 0 or r >=m or c < 0 or c >=n or board[r][c] != word[index]:
#                 return False
            
#             board[r][c] = '#'
            
#             for x,y in dir:
#                 nr = x + r
#                 nc = y + c
#                 if backtrack(index + 1, nr, nc):
#                     return True
#             board[r][c] = word[index]
#             return False        
            
#         for r in range(m):
#             for c in range(n):
#                 if backtrack(0, r,c):
#                     return True
            
#         return False 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def dfs(i, j, index):
#             if index == len(word):
#                 return True
#             if (
#                 i < 0
#                 or i >= len(board)
#                 or j < 0
#                 or j >= len(board[0])
#                 or word[index] != board[i][j]
#             ):
#                 return False
#             temp = board[i][j]
#             board[i][j] = "*"

#             found = (
#                 dfs(i, j - 1, index + 1)
#                 or dfs(i + 1, j, index + 1)
#                 or dfs(i, j + 1, index + 1)
#                 or dfs(i - 1, j, index + 1)
#             )

#             board[i][j] = temp
#             return found

#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if dfs(i, j, 0):
#                     return True
#         return False
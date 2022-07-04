class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        
        def backtrack(r,c,i):  
            if i == len(word):
                return True 
            
            if r < 0 or r >= m or c < 0 or c >=n or board[r][c] != word[i]:
                return False
            
            ch = board[r][c]
            board[r][c] = '#'
            
            for x,y in dir:
                nr = r + x
                nc = c + y
                
                if backtrack(nr,nc,i+1):
                    return True
            board[r][c] = ch 
            
        for r in range(m):
            for c in range(n):
                if backtrack(r,c,0):
                    return True
        return False 
                    
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m = len(board)
#         n = len(board[0])
#         visited = set()
#         dir = [[-1,0],[1,0],[0,-1],[0,1]]
        
#         def backtrack(r,c,i):
            
#             if i == len(word):
#                 return True
            
#             if r < 0 or r >= m or c < 0 or c >= n or (r,c) in visited or board[r][c] != word[i]:
#                 return False
            
#             visited.add((r,c))
#             for x,y in dir:
#                 nr = r + x
#                 nc = c + y
#                 if backtrack(nr,nc,i+1):
#                     return True
#             visited.remove((r,c))
                    
#         for r in range(m):
#             for c in range(n):
#                 if backtrack(r,c,0):
#                     return True
#         return False 
                    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m = len(board)
#         n = len(board[0])
#         dir = [[-1,0], [1,0], [0,-1], [0,1]]
        
        
#         def dfs(r,c,index):
            
#             if index == len(word):
#                 return True
            
#             if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
#                 return False
            
#             ch = board[r][c]
#             board[r][c] = '#'
            
#             for x,y in dir:
#                 nr = r + x
#                 nc = c + y
                
#                 if dfs(nr,nc,index+1):
#                     return True
#             board[r][c] = ch
            
     
        
#         for r in range(m):
#             for c in range(n):
#                 if dfs(r,c,0):
#                     return True
#         return False 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(N* 3^L) where N is the number of cells, L is the length of the word. O(N) to iterate through the board. Each node has three directions to explore except the first node/ch, so the dfs is O(4*3(L-1)), approximately to O(3^L)
#         # O(L) for the recursion call
        
#         m = len(board)
#         n = len(board[0])
#         dir = [[-1,0], [1,0], [0,-1], [0,1]]
        
        
#         # Follow up: use pruning to make the solution faster:
#         d = defaultdict(int)
#         for r in range(m):
#             for c in range(n):
#                 d[board[r][c]] += 1
#         count = Counter(word)
        
#         # if the board doesn't have enough ch for the word
#         if len(word) > m*n:
#             return False
#         # if the ch in word doesn't exist in the board, or the board doesn't have enough ch
#         for ch in word:
#             if not ch in d or d[ch] < count[ch]:
#                 return False
             
                
#         def dfs(r,c,index):
            
#             if index == len(word):
#                 return True
            
#             if r < 0 or r>= m or c < 0 or c >= n:
#                 return False 
            
#             ch = board[r][c]
            
#             if ch != word[index]:
#                 return False
            
#             # mark visited cell
#             board[r][c] = '#'
            
#             for x,y in dir:
#                 nr = r + x
#                 nc = c + y
                
#                 if dfs(nr,nc,index+1):
#                     return True
               
#             board[r][c] = ch 
            
#         for r in range(m):
#             for c in range(n):
#                 if dfs(r,c,0):
#                     return True
#         return False 
                    

        
        
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

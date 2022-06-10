class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        res= 0 
        visited = set()
        dir = [[-1,0], [1,0], [0,-1], [0,1]]
        
        def dfs(r,c):
            
            for x,y in dir:
                nr = r + x
                nc = c + y
                
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dfs(nr, nc)
                    
   
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r,c) not in visited:
                    visited.add((r,c))
                    dfs(r,c)
                    res += 1
        return res 
                    
        
        

                        
                        
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m = len(grid)
#         n = len(grid[0])
#         dir = [[-1,0], [1,0], [0,-1], [0,1]]
        
#         queue = deque()
#         res = 0 
#         # visited = set()
        
#         for row in range(m):
#             for col in range(n):
#                 if grid[row][col] == '1':
#                     grid[row][col] = '0'
#                     res += 1
#                     queue.append((row, col))
                    
#                     while queue:
#                         r,c = queue.popleft()
                        
#                         for x,y in dir:
#                             nr = x + r
#                             nc = y + c
                            
#                             if 0<= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
#                                 # visited.add((nr,nc))
#                                 grid[nr][nc] = '0'
#                                 queue.append((nr,nc))
#         return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m = len(grid)
#         n = len(grid[0])
#         dir = [[-1,0], [1,0], [0,-1], [0,1]]
        
#         def dfs(r,c):
#             grid[r][c] = '0'
            
#             for x,y in dir:
#                 nr = x + r
#                 nc = y + c
                
#                 if 0<= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
#                     dfs(nr, nc)
#         res = 0
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == '1':
#                     dfs(r,c)
#                     res += 1
#         return res 

        
        
        
        
        
        
        
        
        
        
       
        
        
#         m = len(grid)
#         n = len(grid[0])
#         res = 0
#         dir = [[-1,0], [1,0], [0,-1], [0,1]]
#         queue = deque()
#         visited = set()
        
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == '1' and (r,c) not in visited:
#                     res +=1
#                     queue.append((r,c))
                    
#                     while queue:
#                         row, col = queue.popleft()
#                         visited.add((row, col))
                        
#                         for x,y in dir:
#                             nr = x + row
#                             nc = y + col
                            
#                             if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited and grid[nr][nc] == '1':
#                                 queue.append((nr,nc))
#                                 visited.add((nr,nc))
                
#         return res       

                
        
        
        
        
        
        
     
        
        
#         # O(mn), O(mn)
        
#         m = len(grid)
#         n = len(grid[0])
#         dir = [[-1,0], [1,0],[0,-1], [0,1]]
#         res = 0
        
#         def dfs(r,c):
#             grid[r][c] = 0
            
#             for x,y in dir:
#                 nr, nc = x+r, y + c
                
#                 if 0<=nr<m and 0<=nc<n and grid[nr][nc] == "1":
#                     dfs(nr, nc)
        
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == "1":
#                     res +=1
#                     dfs(r,c)
#         return res 
            
            
        
        
        
        
        
        
        
        
        
      
     
        
        
        
        
#         count = 0
#         dir = [(-1,0), (1,0), (0,-1), (0,1)]
        
#         for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 if grid[row][col] == "1":
#                     stack = [(row,col)]
#                     while stack:
#                         r, c = stack.pop()
                        
#                         if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
#                             continue
                            
#                         grid[r][c] = "0"
#                         for x,y in dir:
#                             stack.append((x + r, y + c))
#                     count +=1
                    
#         return count 
                        
       
    
        
        
        
        
        # if not grid:
#             return 0
        
#         result = 0
#         dir = [(-1,0), (1,0), (0,-1), (0,1)]
#         visited = set()
        
#         def dfs (r,c):
#             if r < 0 or r>=len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0" or (r,c) in visited:
#                 return 
#             visited.add((r,c))
            
#             for x,y in dir:
#                 dfs(x+r, y + c)
               
#         for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 if grid[row][col] == "1" and (row, col) not in visited:
#                     dfs(row, col)
#                     result +=1
        
#         return result
    

        
        
        

        
        
        
        
        
       
    
        
        
        
        
        
        
        
        

#         count = 0
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == "1":
#                     self.dfs(grid, r,c)
#                     count+=1
#         return count
    
    
#     def dfs(self, grid, row, column):
#         if row <0 or column <0 or row >=len(grid) or column >= len(grid[0]) or grid[row][column] == "0":
#             return 
        
#         grid[row][column] = "0"
#         self.dfs(grid, row+1, column)
#         self.dfs(grid, row-1, column)
#         self.dfs(grid, row, column + 1)
#         self.dfs(grid, row, column - 1)
        
        
        
        
        
        
        
        
#         if not grid:
#             return 0

#         count = 0
#         for x in range(len(grid)):
#             for y in range(len(grid[0])):
#                 if grid[x][y] == "1":
#                     self.dfs(grid, x, y)
#                     count += 1

#         return count

#     def dfs(self, grid, x, y):
#         if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y] != "1":
#             return

#         grid[x][y] = "#"
#         self.dfs(grid, x + 1, y)
#         self.dfs(grid, x - 1, y)
#         self.dfs(grid, x, y + 1)
#         self.dfs(grid, x, y - 1)
          
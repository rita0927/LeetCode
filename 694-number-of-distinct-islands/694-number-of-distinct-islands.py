class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        res = set()
        dirs = [('u', -1, 0 ), ('d', 1, 0), ('l', 0, -1), ('r', 0, 1)]
        visited = set()
        
        def dfs(r,c,path):
            if r < 0 or r >= m or c < 0 or c >= n or (r,c) in visited or grid[r][c] != 1:
                return 'e'
            
            visited.add((r,c))
            for dir, x, y in dirs:
                nr = x + r
                nc = y + c
                path += dfs(nr, nc, dir)
            
            return path 
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r,c) not in visited:
                    res.add(dfs(r,c,'s'))
                    
        return len(res)
                
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m = len(grid)
#         n = len(grid[0])
#         res = set()
#         directions = [('u',-1, 0), ('d',1,0), ('l',0,-1), ('r',0,1)]
        
#         def bfs(r,c, path):
#             queue = deque([(r,c)])
#             grid[r][c] = 0
            
#             while queue:
#                 r,c = queue.popleft()
#                 for dir, x, y in directions:
#                     nr = x + r
#                     nc = y + c
                    
#                     if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
#                         queue.append((nr, nc))
#                         grid[nr][nc] = 0
#                         path += dir
#                     else:
#                         path += 'e'
#             return path

#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == 1:
#                     res.add(bfs(r,c,'s'))
#         return len(res)
                    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = set()
#         m = len(grid)
#         n = len(grid[0])
        
#         def dfs(r,c,path):
#             if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
#                 return 'e'
#             grid[r][c] = 0
#             u = dfs(r-1,c,'u')
#             d = dfs(r+1,c, 'd')
#             l = dfs(r, c-1, 'l')
#             r = dfs(r, c+1, 'r')
#             path = path + u + d + l + r
#             return path 
       
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == 1:
#                     res.add(dfs(r,c,'s'))
#         return len(res)
                    
        
        
        
        
        
        
        
        
        
        
        
        
#         res = set()
#         m = len(grid)
#         n = len(grid[0])
#         visited = set()
#         directions = [('u',-1, 0), ('d',1,0), ('l',0,-1), ('r',0,1)]
        
#         def dfs(r,c, path):
            
#             if r < 0 or r >= m or c < 0 or c >= n or (r,c) in visited or grid[r][c] == 0:
#                 return 'e'

#             visited.add((r,c))
    
#             for dir, x,y in directions:
#                 nr = r + x
#                 nc = c + y
#                 path += dfs(nr, nc, dir)
#             return path
        
        
        
#         for r in range(m):
#             for c in range(n):
#                  if grid[r][c] == 1 and (r,c) not in visited:
#                         res.add(dfs(r,c, 's'))
#         return len(res)
       
     
        
        
        
#         if not grid:
#             return 0

#         islands = set()
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     path = self.computePath(grid, i, j, "X")
#                     islands.add(path)
#         return len(islands)

#     def computePath(self, grid, i, j, direction):
#         if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
#             return "O"
#         grid[i][j] = 0
#         left = self.computePath(grid, i, j - 1, "L")
#         right = self.computePath(grid, i, j + 1, "R")
#         up = self.computePath(grid, i - 1, j, "U")
#         down = self.computePath(grid, i + 1, j, "D")
#         return direction + left + right + up + down

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m =len(grid)
        n = len(grid[0])
        res = 0
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        
        def helper(r,c):
            nonlocal res 
  
            if (r,c) in visited:
                return
            visited.add((r,c))
            
            for x,y in dir:
                
                nr, nc = x + r, y + c
                
                if nr < 0  or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 0:
                    res +=1
                else:
                    helper(nr, nc)
                             
            
                   
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 1:
                    helper(row, col)
                    return res 

                    
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         self.perimeter = 0
#         visited = set()
#         dir = [(-1,0), (1,0), (0,-1),(0,1)]
        
#         def  helper(r,c):
#             if (r,c) in visited:
#                 return
#             visited.add((r,c))
#             for x,y in dir:
#                 nr = x + r
#                 nc = y +c
                
#                 if nr <0 or nr >= len(grid) or nc <0 or nc >=len(grid[0]) or grid[nr][nc] ==0:
#                     self.perimeter += 1
                
        
#         for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 if grid[row][col] == 1:
#                     helper(row, col)
#         return self.perimeter
        
        
        
        
        
 
        
        
        
        
#         perimeter = 0
#         directions = [(1,0), (-1,0),(0,1), (0,-1)]
        
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == 1:
#                     perimeter +=4
#                     for x,y in directions:
#                         nr, nc = x+r, y +c
#                         if 0<=nr <len(grid) and 0<=nc <len(grid[0]):
#                             perimeter -= grid[nr][nc]
#         return perimeter
        
        
        
        
        
        
        
        
        
        

        
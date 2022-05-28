class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        queue = deque()
        fresh = 0
        time = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh +=1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        
        while queue and fresh:
            
            size = len(queue)
            
            for _ in range(size):
                r,c = queue.popleft()
                
                for x,y in dir:
                    nr = x + r
                    nc = y + c
                    
                    if 0<= nr < m and 0<= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -=1
                        
                        queue.append((nr,nc))
            time +=1
            
        return time if not fresh else -1
            
            
            
 
        
        
        
        
        
        
        
        
        
        

            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



#     # O(m*n), O(m*n) if the grid is filled with rotten oranges 

#         m = len(grid)
#         n = len(grid[0])
#         queue = deque()
#         fresh = 0
#         time = 0
#         dir = [(-1,0), (1,0), (0,-1), (0,1)]
        
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == 1:
#                     fresh +=1
#                 elif grid[r][c] == 2:
#                     queue.append((r,c))
                    
#         while queue and fresh:
#             size = len(queue)
#             for _ in range(size):
#                 r,c = queue.popleft()
                
#                 for x,y in dir:
#                     nr = x + r
#                     nc = y + c
                    
#                     if 0<= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
#                         grid[nr][nc] = 2
#                         fresh -=1
#                         queue.append((nr, nc))
#             time +=1
#         return time if not fresh else -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dir = [(-1,0), (1,0), (0,-1), (0,1)]
#         queue = deque()
        
#         fresh = 0
#         m = len(grid)
#         n = len(grid[0])
        
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == 2:
#                     queue.append((r,c))
#                 elif grid[r][c] == 1:
#                     fresh +=1
#         queue.append((-1, -1))
#         time = -1
        
#         while queue:
#             r,c = queue.popleft()
            
#             if r == -1:
#                 time +=1
#                 if queue:
#                     queue.append((-1,-1))
#             else:
#                 for x, y in dir:
#                     nr = r + x
#                     nc = c + y
                    
#                     if 0<= nr < m and 0<= nc < n:
#                         if grid[nr][nc] == 1:
#                             grid[nr][nc] = 2
#                             fresh -=1
#                             queue.append((nr,nc))
#         return time if not fresh else -1
                    
        
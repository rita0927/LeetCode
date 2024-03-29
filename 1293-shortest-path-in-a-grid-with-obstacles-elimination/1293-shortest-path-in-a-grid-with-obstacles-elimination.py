class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m = len(grid)
        n = len(grid[0])
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = set()
        visited.add((0,0,k))
        
        queue = deque([(0,0,k,0)])
        
        while queue:
            r,c,e,step = queue.popleft()
            
            if [r,c] == [m-1, n-1]:
                return step
            
            for x,y in dir:
                nr = r + x
                nc = c + y
                
                if 0 <= nr < m and 0 <= nc < n:
                    ne = e - grid[nr][nc]
                    if ne >= 0 and (nr,nc,ne) not in visited:
                        queue.append((nr,nc,ne,step+1))
                        visited.add((nr,nc,ne))
            
        return -1        
                
                
                
            
            
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m = len(grid)
#         n = len(grid[0])
#         dest = (m-1, n-1)
#         dir = [[-1,0],[1,0],[0,-1],[0,1]]
        
#         queue= deque([(0,0,k)])
#         seen = set([(0,0,k)])
#         step = -1
#         while queue:
#             size = len(queue)
#             step += 1
#             for _ in range(size):
#                 r,c,eliminator = queue.popleft()
#                 if (r,c) == dest:
#                     return step
#                 for x,y in dir:
#                     nr=r+x
#                     nc=c+y
#                     if 0<=nr<m and 0<=nc<n:
#                         new_eliminator=eliminator-grid[nr][nc]
#                         if new_eliminator >=0 and (nr,nc,new_eliminator) not in seen:
#                             queue.append((nr,nc,new_eliminator))
#                             seen.add((nr,nc,new_eliminator))
#         return -1 
        
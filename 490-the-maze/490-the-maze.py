class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        visited = set()
        dir = [[-1,0], [1,0], [0,-1], [0,1]]
        
        def dfs(r,c):
            
            if [r,c] == destination:
                return True
            visited.add((r,c))
            for x,y in dir:
                nr = r
                nc = c
                
                while 0 <= nr + x < m and 0 <= nc + y < n and maze[nr + x][nc + y] == 0:
                    nr += x
                    nc += y
                
                if (nr, nc) not in visited and dfs(nr,nc):
                    return True
                  
        
        return dfs(start[0], start[1])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m = len(maze)
#         n = len(maze[0])
#         dir =  [[-1,0], [1,0], [0,-1], [0,1]]
#         visited = set()
        
        
#         def dfs(r,c):
            
#             if [r,c] == destination:
#                 return True
            
#             visited.add((r,c))
            
#             for x,y in dir:
#                 nr = r 
#                 nc = c 
                
#                 while 0<= nr + x < m and 0<= nc + y< n and maze[nr + x][nc + y] == 0:
#                     nr += x
#                     nc += y

#                 if (nr, nc) not in visited and dfs(nr,nc):
#                     return True
                

#         return dfs(start[0], start[1])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(mn), O(mn)
        
        
#         m = len(maze)
#         n = len(maze[0])
#         visited = set()
#         dir = [[-1,0], [1,0], [0,-1], [0,1]]
        
#         sr, sc = start
#         queue=deque([(sr, sc)])
        
#         while queue:
#             r,c = queue.popleft()
#             visited.add((r,c))
            
#             if [r,c] == destination:
#                 return True
            
#             for x,y in dir:
#                 nr = r + x
#                 nc = c + y
                
#                 while 0<= nr < m and 0<= nc < n and maze[nr][nc] == 0:
#                     nr += x
#                     nc += y
#                 # deduct the last addition (invalid cell)
#                 nr -= x
#                 nc -= y
#                 if (nr,nc) not in visited:
#                     queue.append((nr, nc))
            
#         return False 
        
        
        
  
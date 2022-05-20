class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        visited = set()
        dir = [[-1,0], [1,0], [0,-1], [0,1]]
        
        queue =deque([(start[0], start[1])])

        while queue:
            r,c = queue.popleft()
            visited.add((r,c))
            
            if [r,c] == destination:
                return True
            
            for x,y in dir:
                nr = r + x
                nc = c + y
                
                while 0<=nr<m and 0<=nc<n and maze[nr][nc] == 0:
                    nr += x
                    nc += y
                nr-=x
                nc-=y
                if (nr,nc) not in visited:
                    queue.append((nr,nc))
                    
        return False 
        
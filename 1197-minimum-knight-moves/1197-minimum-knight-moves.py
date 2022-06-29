class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        res = 0
        dir = [[-2,-1], [-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]
        visited = set()

        queue = deque([(0,0)])
        visited.add((0,0))
        step = 0
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                r,c = queue.popleft()
                
                if [r,c] == [x,y]:
                    return step

                for x1,y1 in dir:
                    nr = r + x1
                    nc = c + y1

                    if (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            step += 1
        
        return step 
                
            
            
            
            
        
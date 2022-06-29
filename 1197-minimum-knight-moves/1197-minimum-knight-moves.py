class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        offsets = [[-2,-1], [-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]
        
        origin_queue = deque([(0, 0, 0)])
        origin_distance = {(0, 0): 0}
        
        target_queue = deque([(x, y, 0)])
        target_distance = {(x, y): 0}
        
        while origin_queue or destQ:
            r1, c1, step1 = origin_queue.popleft()
            if (r1,c1) in target_distance:
                return step1 + target_distance[(r1,c1)]
            
            r2,c2,step2 = target_queue.popleft()
            if (r2,c2) in origin_distance:
                return step2 + origin_distance[(r2,c2)]
            
            for x1,y1 in offsets:
                nr1 = r1 + x1
                nc1 = c1 + y1
                
                if (nr1,nc1) not in origin_distance:
                    origin_queue.append((nr1,nc1,step1+1))
                    origin_distance[(nr1, nc1)] = step1+1
                
                nr2 = r2 + x1
                nc2 = c2 + y1
                
                if (nr2,nc2) not in target_distance:
                    target_queue.append((nr2,nc2,step2+1))
                    target_distance[(nr2,nc2)] = step2 + 1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = 0
#         dir = [[-2,-1], [-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]
#         visited = set()

#         queue = deque([(0,0)])
#         visited.add((0,0))
#         step = 0
        
#         while queue:
#             size = len(queue)
            
#             for _ in range(size):
#                 r,c = queue.popleft()
                
#                 if [r,c] == [x,y]:
#                     return step

#                 for x1,y1 in dir:
#                     nr = r + x1
#                     nc = c + y1

#                     if (nr,nc) not in visited:
#                         visited.add((nr,nc))
#                         queue.append((nr,nc))
#             step += 1
        
#         return step 
                
            
            
            
            
        
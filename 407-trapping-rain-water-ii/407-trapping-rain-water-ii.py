class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        dir = [[-1,0],[1,0],[0,-1], [0,1]]
        heap = []
        res = 0
        visited = set()
        
        
        for r in range(m):
            for c in range(n):
                if r == 0 or r  == m - 1 or c == 0 or c == n-1:
                    heappush(heap, [heightMap[r][c], r,c])
                    visited.add((r,c))

        while heap:
            h,r,c = heappop(heap)
            for x,y in dir:
                nr = r + x 
                nc = c + y
                
                if 0<= nr < m and 0 <= nc <n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    heappush(heap,[max(h,heightMap[nr][nc]), nr,nc])
                    res += max(0, h-heightMap[nr][nc])
        return res
                    
        
                
        
        
        
        
        
        
        
        
        
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        m = len(heightMap)
        n = len(heightMap[0])
        dir = [[-1,0],[1,0],[0,-1], [0,1]]
        visited = set()
        res = 0
        heap = []
        
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    heappush(heap, [heightMap[r][c], r,c])
                    visited.add((r,c))
        while heap:
            h,r,c = heappop(heap)
            
            for x,y in dir:
                nr = r + x
                nc = c + y 
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    res += max(0, h - heightMap[nr][nc])
                    heappush(heap, [max(h,heightMap[nr][nc]), nr,nc])
        return res 
        
        

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''
1. 矩阵四边是不能存水的。
2. 矩阵四边形成一个桶，桶高$h$为四边中最低边。
3. 对四边中最低边的邻居单元格，
    - 如果高度$s$低于$h$，可放入水量$h-s$，将该单元格高度改为$h$取代原来桶边（四边最低边）构造新桶，
    - 如果高度$s$高于$h$，不可放水，可取代原来桶边（四边最低边）构造新桶。

当新单元格高度$s$低于原桶边高度$h$，第三步的做法相当于在新单元格上存满水，以其作为新桶边构造新桶。
   
'''      
        
        
        
        
#         # O(mnlog(mn)), every cell is pushed and popped from the heap
#         # O(mn)
#         m = len(heightMap)
#         n = len(heightMap[0])
#         dir = [[-1,0],[1,0],[0,-1], [0,1]]
#         heap = []
#         res = 0
#         visited = set()
        
#         # edges can't store water
#         for r in range(m):
#             for c in range(n):
#                 if r == 0 or r  == m - 1 or c == 0 or c == n-1:
#                     heappush(heap, [heightMap[r][c], r,c])
#                     visited.add((r,c))

#         while heap:
#             # assume the edges construct a bucket, the shortted edge matters the most 
#             # pop out the min_hight from the current edges
#             # visit all cells inside, replace the shorter edges with taller inner cell
#             h,r,c = heappop(heap)
#             for x,y in dir:
#                 nr = r + x 
#                 nc = c + y
                
#                 if 0<= nr < m and 0 <= nc <n and (nr,nc) not in visited:
#                     visited.add((nr,nc))
                    
#                     # if neighbor is taller, form a new edge to replace the previous edge
#                     # if neighbor is shorter, store water in this neighbor cell 
#                     heappush(heap,[max(h,heightMap[nr][nc]), nr,nc])
#                     res += max(0, h-heightMap[nr][nc])
#         return res
                    
        
                
        
        
        
        
        
        
        
        
        
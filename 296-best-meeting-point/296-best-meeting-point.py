class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        rows = []
        cols = []
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    rows.append(r)
                    
        for c in range(n):
            for r in range(m):
                if grid[r][c] == 1:
                    cols.append(c)
                    
        def minDist(lst):
            l = 0
            r = len(lst) - 1
            dist = 0
            while l < r:
                dist+= lst[r] - lst[l]
                l+=1
                r-=1
            return dist
        
        return minDist(rows) + minDist(cols)
                
        
        
#         mid_row = rows[len(rows)//2]
#         mid_col = cols[len(cols)//2]
        
#         def minDist(lst, mid):
#             dist = 0
#             for p in lst:
#                 dist+= abs(p-mid)
#             return dist
        
#         return minDist(rows, mid_row) + minDist(cols, mid_col)
        
        
        
        
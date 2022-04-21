class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        
        m = len(image)
        n = len(image[0])
        color = image[sr][sc]
        queue = deque([(sr,sc)])
        
        while queue:
            r,c = queue.popleft()
            if image[r][c] == color:
                image[r][c] = newColor
                
                if r- 1>=0:
                    queue.append((r-1, c))
                if r + 1 < m:
                    queue.append((r + 1, c))
                if c - 1 >=0:
                    queue.append((r, c -1))
                if c + 1 < n:
                    queue.append((r, c + 1))
                
        return image 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if image[sr][sc] == newColor:
#             return image
        
#         m = len(image)
#         n = len(image[0])
#         dir = [(-1,0), (1,0), (0,-1),(0,1)]
#         color = image[sr][sc]
        
#         def helper(r,c):
#             image[r][c] = newColor
            
#             for x,y in dir:
#                 nr = x + r
#                 nc = y + c
                
#                 if 0<= nr < m and 0 <=nc <n and image[nr][nc] == color:
#                     helper(nr, nc)
#         helper(sr, sc)
        
#         return image 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m = len(image)
#         n = len(image[0])
        
#         # record original color
#         origin = image[sr][sc]
        
#         if origin == newColor:
#             return image
        
#         #dfs 
#         def dfs(r,c):
#             if image[r][c] == origin:
#                 image[r][c] = newColor
#         # if within the range & has original color
#                 if r > 0:
#                     dfs(r-1,c)
#                 if r < m - 1:
#                     dfs(r+1, c)
#                 if c > 0:
#                     dfs(r, c-1)
#                 if c < n - 1:
#                     dfs(r, c+1)
#         dfs(sr,sc)
#         return image 



#         m = len(image)
#         n = len(image[0])
        
#         origin = image[sr][sc]
        
#         if origin == newColor:
#             return image
        
#         stack = [(sr,sc)]
        
#         while stack:
#             r,c = stack.pop()
            
#             if image[r][c]==origin:
#                 image[r][c] = newColor
                
#                 if r > 0:
#                     stack.append((r-1,c))
#                 if r < m - 1:
#                     stack.append((r+1, c))
#                 if c > 0:
#                     stack.append((r, c-1))
#                 if c < n - 1:
#                     stack.append((r, c+1))
                
#         return image 
    
        
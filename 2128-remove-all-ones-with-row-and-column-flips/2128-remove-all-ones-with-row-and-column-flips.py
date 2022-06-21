class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        
        origin = grid[0]
        flip = [1-x for x in grid[0]]
        
        for r in grid:
            if r != origin and r != flip:
                return False
            
        return True 
        
        
        
        
        
        
        

        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # each pair of rows have to be the same or completely opposite, then the flip can make them the same

#         row_ori = grid[0]
#         row_flip = [1-x for x in grid[0]]
        
#         for r in grid[1:]:
#             if r != row_ori and r != row_flip:
#                 return False
#         return True 
            
        
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:

        row_ori = grid[0]
        row_flip = [1-x for x in grid[0]]
        
        for r in grid[1:]:
            if r != row_ori and r != row_flip:
                return False
        return True 
            
        
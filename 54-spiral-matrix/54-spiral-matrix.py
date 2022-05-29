class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top +=1
        
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -=1
            
            # make sure the row has not been traversed
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            # make sure the col has not already been traversed
            if left <= right:
                for i in range(bottom, top -1, -1):
                    res.append(matrix[i][left])
                left +=1
        
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
#         left = 0
#         right = len(matrix[0]) - 1
#         top = 0
#         bottom = len(matrix) - 1

#         while left <= right and top <= bottom:
#             for i in range(left, right + 1):
#                 res.append(matrix[top][i])
#             top += 1

#             for i in range(top, bottom + 1):
#                 res.append(matrix[i][right])
#             right -= 1

#             if top <= bottom:
#                 for i in range(right, left - 1, -1):
#                     res.append(matrix[bottom][i])
#                 bottom -= 1

#             if left <= right:
#                 for i in range(bottom, top - 1, -1):
#                     res.append(matrix[i][left])
#                 left += 1

#         return res
        
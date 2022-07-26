class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        i1 = 0
        i2 = 0
        res = []
        
        while i1 < len(firstList) and i2 < len(secondList):
            l = max(firstList[i1][0], secondList[i2][0])
            r = min(firstList[i1][1], secondList[i2][1])
            
            if l <= r:
                res.append([l,r])
            
            if firstList[i1][1] < secondList[i2][1]:
                i1 += 1
            else:
                i2 += 1
        
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(M+N)
        
#         res = []
#         i1 = 0
#         i2 = 0
        
#         while i1 < len(firstList) and i2 < len(secondList):
#             l = max(firstList[i1][0], secondList[i2][0])
#             r = min(firstList[i1][1], secondList[i2][1])
            
#             if l <= r:
#                 res.append([l,r])
            
#             if firstList[i1][1] < secondList[i2][1]:
#                 i1 += 1
#             else:
#                 i2 += 1
        
#         return res 
                
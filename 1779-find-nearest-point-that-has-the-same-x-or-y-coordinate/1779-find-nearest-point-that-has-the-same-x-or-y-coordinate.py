class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        distance = float('inf')
        res = -1
        
        for i, point in enumerate(points):
            x1, y1 = point
            
            if x1 == x or y1 == y:
                d1 = abs(x1-x) + abs(y1-y)
                if d1 < distance:
                    distance = d1
                    res = i
        return res 

            
        
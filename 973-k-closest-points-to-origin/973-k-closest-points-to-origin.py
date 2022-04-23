class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = sorted(points, key = lambda x: x[0] **2 + x[1] **2)
        
        return distances[:k]
        
        
#         points.sort(key = lambda x: x[0]**2 + x[1]**2)

#         return points[:k]


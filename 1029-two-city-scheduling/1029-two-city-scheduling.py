class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda x: x[0] - x[1])
        
        mid = len(costs)//2
        
        res = 0
        for i in range(mid):
            res += costs[i][0] + costs[mid + i][1]
        
        return res 
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         costs.sort(key = lambda x: x[0]-x[1])
           
#         total = 0
#         for i in range(len(costs)//2):
#             total += costs[i][0] + costs[-i-1][1]
#         return total 
            
            
        
        
        
        
      
        
        
        
        
#         # O(NlogN), O(logN) for sorting 
        
#         # sort by opportunity gain by sending to A instead of B
#         costs.sort(key = lambda x: x[0] - x[1])
        
#         total = 0
#         mid = len(costs)//2
#         for i in range(mid):
#             total += costs[i][0] + costs[i + mid][1]
#         return total 
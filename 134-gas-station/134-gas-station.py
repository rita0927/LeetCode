class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        rem = 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i+ 1
                tank = 0
                
            rem += gas[i] - cost[i]
            
        return start if rem >= 0 else -1
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         total = 0
#         tank = 0
#         start = 0

#         for i in range(len(gas)):
#             tank += gas[i] - cost[i]

#             if tank < 0:
#                 start = i + 1
#                 tank = 0

#             total += gas[i] - cost[i]

#         return start if total >= 0 else -1
        
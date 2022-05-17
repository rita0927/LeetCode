class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_tank = 0
        start = 0
        total_tank = 0
        
        for i in range(len(gas)):
            cur_tank += gas[i] - cost[i]
            # If current start can't get there
            if cur_tank < 0:
                # Pick up the next station as the start
                start = i+ 1
                # Start with an empty tank
                cur_tank = 0
                
            total_tank += gas[i] - cost[i]
            
        return start if total_tank >= 0 else -1
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9+7
        neighbors = {
            0: [4,6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [0,3,9],
            5: [],
            6: [0,1,7],
            7: [2,6],
            8: [1,3],
            9 :[2,4]
        }
        
        cur = [1]*10
        
        for i in range(n-1):
            next = [0]*10
            
            for i in range(10):
                for neighbor in neighbors[i]:
                    next[i] += cur[neighbor]%mod
            cur = next
            
        return sum(cur)%mod 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n), O(1)
        
#         mod = 10 ** 9 + 7
#         # map the starting key and the list of destination keys 
#         neighbors = {
#             0: (4,6),
#             1: (6,8),
#             2: (7,9),
#             3: (4,8),
#             4: (0,3,9),
#             5: (),
#             6: (0,1,7),
#             7: (2,6),
#             8: (1,3),
#             9: (2,4),          
#         }
        
#         # place the knight on any numeric cell initially 
#         cur = [1] * 10
        
#         # the first dile is to place the knight on the cell, then perform n-1 jumps
#         for _ in range(n - 1):
#             next = [0] * 10
            
#             for start in range(10):
#                 for end in neighbors[start]:
#                     next[end] = (next[end] + cur[start])%mod
#             cur = next 
#         return sum(cur) %mod
            
        
    
        
        
        
        
        
        
        
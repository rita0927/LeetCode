class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
  
        pairMap = defaultdict(int)
        preferMap = defaultdict(dict)
        
        for x,y in pairs:
            pairMap[x] = y
            pairMap[y] = x
            
        
        for x in range(n):
            for index, y in enumerate(preferences[x]):
                preferMap[x][y] = index 
        
        res = 0
        for x in range(n):
            for y in preferences[x]:
                pair = pairMap[x]
                y_pair = pairMap[y]
                
                if preferMap[x][y] < preferMap[x][pair] and preferMap[y][x] < preferMap[y][y_pair]:
                    res += 1
                    break
        return res 
                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n^2), O(n^2)
        
#         pairMap = defaultdict(int)
#         preferMap = defaultdict(dict)
        
#         # pair map 
#         for x,y in pairs:
#             pairMap[x] = y
#             pairMap[y] = x
        
#         # preference map, e.g. {0: {1:0, 2:1, 3:2}, 1: {3:0, 2;1, 0:2}}
#         for i in range(n):
#             for j in range(n-1):
#                 prefer = preferences[i][j]
#                 preferMap[i][prefer] = j
                
#         res = 0
        
#         for i in range(n):
#             for j in range(n-1):
                
#                 # find pair, preferred friend, preferred friend's pair 
#                 pair = pairMap[i]
#                 prefer = preferences[i][j]
#                 preferPair = pairMap[prefer]
                
#                 # prefer each other than their current pair 
#                 if preferMap[i][prefer] < preferMap[i][pair] and preferMap[prefer][i] < preferMap[prefer][preferPair]:
#                     res += 1
#                     break
#         return res 
        
                
        
        
        
        
        
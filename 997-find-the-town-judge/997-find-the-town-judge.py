class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # need at least n-1 edges/trust for a judge to be trusted by others 
        if len(trust) < n-1:
            return -1
        
        # potential judge (represented by index) being trusted by indegree[judge] people 
        indegree = [0] * (n+1)
        # people who trust outdegree[people]
        outdegree = [0] * (n+1)
        
        for p, j in trust:
            outdegree[p]+=1
            indegree[j] +=1
        print(outdegree)
        print(indegree)
        for i in range(1, n+1):
            # if indegree[judge] == n-1: trusted by everyone else 
            # if outdegree[people] == 0: don't trust others 
            
            # if more than one indegree[i] == n-1, won't have any judge with 0 outdegree 
            # if more than one outdegree[i] == 0, won't have any people with n-1 indegree
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        return -1 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if n == 1:
#             return 1
        
#         judges  = defaultdict(int)
#         people = set()
        
#         for p, j in trust:
#             people.add(p)
#             judges[j] +=1

#         res = None
#         for j in judges:
#             if judges[j] == n-1 and j not in people:
#                 if not res:
#                     res = j
#                 else:
#                     return -1
#         return res if res else -1 
                
        
        
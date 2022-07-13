class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        degree = defaultdict(int)
        
        for a,b in trust:
            degree[a] -= 1
            degree[b] += 1
        

        for i in range(1,n+1):
            if degree[i] == n-1:
                return i
        return -1
            

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(trust) < n-1:
#             return -1
        
#         degree = [0] * (n+1)
        
#         for i,j in trust:
#             degree[i] -= 1
#             degree[j] += 1
        
#         for i in range(1,n+1):
#             if degree[i] == n-1:
#                 return i
#         return -1 
        
        
        
        
     
        
        
        
        
#         if len(trust) < n-1:
#             return -1
            
#         degree = [0] * (n+1)
        
#         # degree[p] -= 1 is p trusts others, degree[p] += 1 when p is trusted by others
#         # judge has to earn all the score from others, + (n-1), and don't lose any score, - 0
#         for i, j in trust:
#             degree[i] -= 1
#             degree[j] += 1
        
#         for i in range(1,len(degree)):
#             if degree[i] == n-1:
#                 return i
#         return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(E) where E is the number of edges (len of trust). If N-1 > E, return right away (0(1)). Otherwise, O(N + E) don't know whether E or N is the bigger one. Since E >= N-1, E is bigger, and the final is O(max(N, E)), so it's O(E)
#         # O(N)
        
#         # need at least n-1 edges/trust for a judge to be trusted by others 
#         # not enough edges to generate one judge
#         if len(trust) < n-1:
#             return -1
        
#         # potential judge (represented by index) being trusted by indegree[judge] people 
#         indegree = [0] * (n+1)
#         # people who trust outdegree[people]
#         outdegree = [0] * (n+1)
        
#         for p, j in trust:
#             outdegree[p]+=1
#             indegree[j] +=1

#         for i in range(1, n+1):
#             # if indegree[judge] == n-1: trusted by everyone else 
#             # if outdegree[people] == 0: don't trust others 
            
#             # if more than one indegree[i] == n-1, won't have any judge with 0 outdegree 
#             # if more than one outdegree[i] == 0, won't have any people with n-1 indegree
#             if indegree[i] == n-1 and outdegree[i] == 0:
#                 return i
#         return -1 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if n == 1:
#             return 1
        
#         judges  = defaultdict(int)
#         people = set()
        
#         for p, j in trust:
#             people.add(p)
#             judges[j] +=1

#         for j in range(1, n+1):
#             if judges[j] == n-1 and j not in people:
#                 return j
#         return  -1 
                
        
        
class Solution:
     
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        res = 0
        visited = set()
              
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            

        for i in range(n):
            if i not in visited:
                res +=1
                stack = [i]
                while stack:
                    node = stack.pop()
                    visited.add(node)
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
  
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         parents = [i for i in range(n)]
#         rank = [1] * n
        
#         def find(n1):
#             root = n1
#             while root != parents[root]:
#                 parents[root] = parents[parents[root]]
#                 root = parents[root]
#             return root
        
#         def union(n1, n2):
#             p1, p2 = find(n1), find(n2)
            
#             if p1 == p2:
#                 return 0
            
#             if rank[p2] > rank[p1]:
#                 parents[p1] = p2
#                 rank[p2] +=rank[p1]
#             else:
#                 parents[p2] = p1
#                 rank[p1] += rank[p2]
#             return 1
        
#         res = n
#         for n1, n2 in edges:
#             res -= union(n1, n2)
        
#         return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         adj = defaultdict(list)
#         res = 0
#         visited = set()
        
#         for a,b in edges:
#             adj[a].append(b)
#             adj[b].append(a)
             
#         for i in range(n):
#             if i not in visited:
#                 stack = [i]
#                 while stack:
#                     node = stack.pop()
#                     visited.add(node)    
#                     for neighbor in adj[node]:
#                         if neighbor not in visited:
#                             stack.append(neighbor)
#                 res +=1
#         return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         neighbors = defaultdict(list)
#         res = 0
#         visited = set()
        
#         for a, b in edges:
#             neighbors[a].append(b)
#             neighbors[b].append(a)
        
#         def dfs(node):
#             visited.add(node)
#             for neighbor in neighbors[node]:
#                 if neighbor not in visited:
#                     dfs(neighbor)
        
        
#         for i in range(n):
#             if i not in visited:
#                 dfs(i)
#                 res +=1
#         return res 
    
    
"""
0(E+V): when we iterate over the edge list of each vertex, we look at each edge once. This has a total cost of O(E+V). Building the adjacency list will take O(E) operations, as we iterate over the list of edges. During the DFS traversal, each vertex will only be visited once, 0(V)

O(E+V): Building the adjacency list will take O(E) space. To keep track of visited vertices, an array of size O(V) is required. Also, the run-time stack for DFS will use O(V) space.

"""
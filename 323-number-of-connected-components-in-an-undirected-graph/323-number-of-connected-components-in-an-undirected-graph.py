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
                stack = [i]
                while stack:
                    node = stack.pop()
                    visited.add(node)    
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                res +=1
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
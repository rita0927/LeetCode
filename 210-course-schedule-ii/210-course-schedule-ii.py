class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        indegree = defaultdict(int)
        
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs]+=1
        
        queue = deque()
        for crs in range(numCourses):
            if not indegree[crs]:
                queue.append(crs)
        
        res = []
        while queue:
            pre = queue.popleft()
            res.append(pre)
            
            for crs in adj[pre]:
                indegree[crs] -= 1
                if not indegree[crs]:
                    queue.append(crs)
                    
            
        return res if len(res) == numCourses else []


                
                
        
        
        
        
        
        
        
        

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
# # O(E + V), O(E + V)
# # When there's a cycle, in_degree[cycled_crs] won't be 0 or added to the queue/res 

#         adj_list = defaultdict(list)
#         indegree = {}
#         res = []
        
#         for crs, pre in prerequisites:
#             adj_list[pre].append(crs)
#             indegree[crs] = indegree.get(crs, 0) + 1
        
#         queue = deque([c for c in range(numCourses) if c not in indegree])
        
#         while queue:
#             pre = queue.popleft()
#             res.append(pre)
            
#             for crs in adj_list[pre]:
#                 indegree[crs] -=1
                
#                 if indegree[crs] == 0:
#                     queue.append(crs)
            
                    
#         return res if len(res) == numCourses else []
        
        
        
        
        
        
        

#         adj_list = defaultdict(list)
#         visited, cycle = set(), set()
#         res = []
        
#         for crs, pre in prerequisites:
#             adj_list[crs].append(pre)
        
#         def dfs(crs):
            
#             if crs in cycle:
#                 return False
#             if crs in visited:
#                 return True
            
#             cycle.add(crs)
#             for pre in adj_list[crs]:
#                 if not dfs(pre):
#                     return False
#             cycle.remove(crs)
#             visited.add(crs)
#             res.append(crs)
#             return True
        
        
#         for crs in range(numCourses):
#             if not dfs(crs):
#                 return []
#         return res
        
        
    
        
        
        
    


            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

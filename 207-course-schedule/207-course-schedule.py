class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        indegree = defaultdict(int)
        
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        
        queue = deque()
        for crs in range(numCourses):
            if not indegree[crs]:
                queue.append(crs)
        
        visited = set()
        while queue:
            pre = queue.popleft()
            visited.add(pre)
            for crs in adj[pre]:
                indegree[crs] -= 1
                
                if indegree[crs] == 0:
                    queue.append(crs)
                    
        return len(visited) == numCourses
            
            
        


        
        

            
            

            
        

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         adj = defaultdict(list)
#         indegree = defaultdict(int)
        
#         for crs, pre in prerequisites:
#             adj[pre].append(crs)
#             indegree[crs]+=1
        
#         queue = deque([])
#         seen = set()
        
#         for i in range(numCourses):
#             if i not in indegree:
#                 queue.append(i)
        
#         while queue:
#             pre = queue.popleft()
#             seen.add(pre)
#             for crs in adj[pre]:
#                 indegree[crs] -= 1
                
#                 if not indegree[crs]:
#                     queue.append(crs)
                    
#         return len(seen) == numCourses     
        
        
        
        
        
        
        
        

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#  O(V+E), O(V+E)       
#         adj_list = defaultdict(list)
#         indegree = {}
        
#         for crs, pre in prerequisites:
#             adj_list[pre].append(crs)
#             indegree[crs] = indegree.get(crs, 0) + 1
            
#         queue = deque([c for c in range(numCourses) if c not in indegree ])
#         visited = set()
        
#         while queue:
            
#             pre = queue.popleft()
#             visited.add(pre)
            
#             for crs in adj_list[pre]:
#                 indegree[crs] -=1
                
#                 if indegree[crs] == 0:
#                     queue.append(crs)               
        
#         return len(visited) == numCourses 
            
        
        
        
        
        
        
     
        
# O(V+ E), O(V+E)      
        
#         adj_list = defaultdict(list)
#         visited = set()
        
#         for crs, pre in prerequisites:
#             adj_list[crs].append(pre)
        
        
#         def dfs(crs):
#             if crs in visited:
#                 return False
#             visited.add(crs)
#             for pre in adj_list[crs]:
#                 if not dfs(pre):
#                     return False
#             adj_list[crs] = []
#             visited.remove(crs)
#             return True
            
#         for crs in range(numCourses):
#             if not dfs(crs):
#                 return False
#         return True
        
        
 
        
        
        
        
        
        
        
        
        
        
#         preMap = {i: [] for i in range(numCourses)}

#         for crs, pre in prerequisites:
#             preMap[crs].append(pre)

#         visited = set()

#         def dfs(crs):
#             if crs in visited:
#                 return False
#             if preMap[crs] == []:
#                 return True
#             visited.add(crs)
#             for pre in preMap[crs]:
#                 if not dfs(pre):
#                     return False
#             visited.remove(crs)
#             preMap[crs] = []
#             return True

#         for crs in range(numCourses):
#             if not dfs(crs):
#                 return False

#         return True

        
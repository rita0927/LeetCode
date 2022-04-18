class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = defaultdict(list)
        visited, cycle = set(), set()
        res = []
        
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        def dfs(crs):
            
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
        
        
    
        
        
        
        
        
        
#         indegree = {}
#         adj_list = defaultdict(list)
#         res = []
        
#         for crs, pre in prerequisites:
#             indegree[crs] = indegree.get(crs, 0) + 1
#             adj_list[pre].append(crs)
        
#         queue =deque([c for c in range(numCourses) if c not in indegree])
        
#         while queue:
#             pre = queue.popleft()
#             res.append(pre)
            
#             for crs in adj_list[pre]:
#                 indegree[crs] -=1
#                 if indegree[crs] == 0:
#                     queue.append(crs)
        
#         return res if len(res) == numCourses else []
                    


            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

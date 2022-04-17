class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsGraph = defaultdict(list)
        
        for crs, pre in prerequisites:
            crsGraph[crs].append(pre)
        
        visited, cycle = set(), set()
        res = []
        
        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for pre in crsGraph[crs]:
                if not dfs(pre):
                    return False
            
            crsGraph[crs] = []
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
            
    
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
            
        
        

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         crsMap = {c: [] for c in range(numCourses)}
        
#         for crs, pre in prerequisites:
#             crsMap[crs].append(pre)
            
#         res = []
#         visited, cycle = set(), set()
        
#         def dfs(crs):
#             if crs in cycle:
#                 return False
#             if crs in visited:
#                 return True
            
#             cycle.add(crs)
#             for pre in crsMap[crs]:
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
            
            
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
     
        
        
#       preMap = [[] for _ in range(numCourses)]

#       for crs, pre in prerequisites:
#         preMap[pre].append(crs)

#       visited = set()
#       tracker = set()
#       stack = []
#       self.hasCycle=False

#       def dfs (crs, visited, tracker, stack):
#         visited.add(crs)
#         tracker.add(crs)
#         for nx in preMap[crs]:
#           if nx in tracker:
#             self.hasCycle=True
#             break
#           if nx not in visited:
#             dfs(nx, visited, tracker, stack)
#         tracker.remove(crs)
#         stack.append(crs)


#       for crs in range(numCourses):
#         if crs not in visited:
#           dfs(crs, visited, tracker, stack)
#       if self.hasCycle:
#         return []
#       return stack [::-1]
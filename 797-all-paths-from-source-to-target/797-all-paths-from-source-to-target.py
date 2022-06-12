class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        
        def backtrack(num, path):
            
            if num == n-1:
                res.append(path.copy())
                return

            for neighbor in graph[num]:

                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()

        backtrack(0,[0])
        return res 
            
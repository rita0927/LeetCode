class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        res = 0
        visited = set()
        
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(node):
            visited.add(node)
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                res +=1
        return res 
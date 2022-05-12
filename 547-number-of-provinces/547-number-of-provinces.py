class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parents = [i for i in range(n)]
        rank = [1] * n
        
        def find(n1):
            root = n1
            while root != parents[root]:
                parents[root] = parents[parents[root]]
                root = parents[root]
            return root
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for r in range(n):
            for c in range(r + 1, n):
                if isConnected[r][c] == 1:
                    res -= union(r, c)
                    
        return res 
                
        
        